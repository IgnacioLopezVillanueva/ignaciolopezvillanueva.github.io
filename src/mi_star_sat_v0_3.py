#!/usr/bin/env python3
"""MI*-SAT v0.3: standalone educational SAT solver with incremental structures."""
from __future__ import annotations

import argparse
import time
import sys
from dataclasses import dataclass
from typing import List, Dict, Optional, Tuple, Set

sys.setrecursionlimit(20000)


@dataclass
class CNF:
    nvars: int
    clauses: List[List[int]]


def parse_dimacs(path: str) -> CNF:
    clauses: List[List[int]] = []
    nvars = None
    declared = None
    current: List[int] = []

    with open(path, "r", encoding="utf-8", errors="replace") as f:
        for raw in f:
            line = raw.strip()
            if not line or line.startswith("c"):
                continue
            if line.startswith("p"):
                parts = line.split()
                if len(parts) != 4 or parts[1] != "cnf":
                    raise ValueError("Cabecera DIMACS inválida")
                nvars = int(parts[2])
                declared = int(parts[3])
                if nvars < 0 or declared < 0:
                    raise ValueError("Dimensiones DIMACS inválidas")
                continue
            if nvars is None:
                raise ValueError("Falta la cabecera DIMACS")
            for token in line.split():
                lit = int(token)
                if lit == 0:
                    clauses.append(current)
                    current = []
                else:
                    if abs(lit) > nvars:
                        raise ValueError(f"Literal {lit} fuera del rango de variables")
                    current.append(lit)

    if nvars is None:
        raise ValueError("Falta la cabecera DIMACS")
    if current:
        raise ValueError("Cláusula DIMACS sin terminador 0")
    if declared is not None and len(clauses) != declared:
        raise ValueError(
            f"La cabecera declara {declared} cláusulas, pero se han leído {len(clauses)}"
        )
    return CNF(nvars, clauses)


class MIStarSolverIncremental:
    def __init__(self, cnf: CNF, heuristic: str = "mistar"):
        self.cnf = cnf
        self.heuristic = heuristic
        self.nvars = cnf.nvars
        self.assignment: Dict[int, bool] = {}
        self.clause_satisfied = [False] * len(cnf.clauses)
        self.clause_lit_count = [len(c) for c in cnf.clauses]

        self.occurs: Dict[int, List[int]] = {
            i: [] for i in range(1, self.nvars + 1)
        }
        for c_idx, clause in enumerate(cnf.clauses):
            for lit in clause:
                self.occurs[abs(lit)].append(c_idx)

        self.init_pos = [0] * (self.nvars + 1)
        self.init_neg = [0] * (self.nvars + 1)
        self.activity = [0.0] * (self.nvars + 1)
        self.polarity = [0] * (self.nvars + 1)

        for clause in cnf.clauses:
            for lit in clause:
                if lit > 0:
                    self.init_pos[lit] += 1
                else:
                    self.init_neg[abs(lit)] += 1

        self.decisions = 0
        self.nodes = 0
        self.conflicts = 0
        self.total_choose_time = 0.0
        self.total_propagate_time = 0.0
        self.start_time = 0.0

    def _assign(self, v: int, val: bool,
                trail: List[Tuple[int, List[int], List[int]]]):
        self.assignment[v] = val
        sat_clauses = []
        reduced_clauses = []

        for c_idx in self.occurs[v]:
            if self.clause_satisfied[c_idx]:
                continue
            is_satisfied = any(
                abs(lit) == v and (lit > 0) == val
                for lit in self.cnf.clauses[c_idx]
            )
            if is_satisfied:
                self.clause_satisfied[c_idx] = True
                sat_clauses.append(c_idx)
            else:
                self.clause_lit_count[c_idx] -= 1
                reduced_clauses.append(c_idx)

        trail.append((v, sat_clauses, reduced_clauses))

    def _unassign(self, state: Tuple[int, List[int], List[int]]):
        v, sat_clauses, reduced_clauses = state
        self.assignment.pop(v, None)
        for c_idx in sat_clauses:
            self.clause_satisfied[c_idx] = False
        for c_idx in reduced_clauses:
            self.clause_lit_count[c_idx] += 1

    def _propagate(self, trail: List[Tuple[int, List[int], List[int]]]) -> bool:
        t0 = time.perf_counter()
        changed = True
        while changed:
            changed = False
            for c_idx, clause in enumerate(self.cnf.clauses):
                if self.clause_satisfied[c_idx]:
                    continue
                if self.clause_lit_count[c_idx] == 0:
                    self.conflicts += 1
                    for lit in clause:
                        self.activity[abs(lit)] += 1.0
                    self.total_propagate_time += time.perf_counter() - t0
                    return False
                if self.clause_lit_count[c_idx] == 1:
                    unassigned_lit = next(
                        (lit for lit in clause if abs(lit) not in self.assignment),
                        None
                    )
                    if unassigned_lit is not None:
                        v = abs(unassigned_lit)
                        self._assign(v, unassigned_lit > 0, trail)
                        changed = True
                        break
        self.total_propagate_time += time.perf_counter() - t0
        return True

    def _get_incremental_graph(self) -> Tuple[Set[int], Dict[int, Set[int]]]:
        active: Set[int] = set()
        adj: Dict[int, Set[int]] = {}
        for c_idx, clause in enumerate(self.cnf.clauses):
            if self.clause_satisfied[c_idx]:
                continue
            vars_ = [
                abs(lit) for lit in clause
                if abs(lit) not in self.assignment
            ]
            if not vars_:
                continue
            for v in vars_:
                active.add(v)
                adj.setdefault(v, set())
            for i, u in enumerate(vars_):
                for w in vars_[i + 1:]:
                    adj[u].add(w)
                    adj[w].add(u)
        return active, adj

    def _choose(self) -> Optional[int]:
        t0 = time.perf_counter()
        active, adj = self._get_incremental_graph()
        if not active:
            self.total_choose_time += time.perf_counter() - t0
            return None

        maxdeg = max((len(adj.get(v, ())) for v in active), default=1) or 1
        maxact = max((self.activity[v] for v in active), default=1.0) or 1.0
        best_v = None
        best_score = -float("inf")

        if self.heuristic == "activity":
            for v in active:
                degree = len(adj.get(v, ()))
                score = self.activity[v] / maxact + 0.001 * degree / maxdeg
                if score > best_score:
                    best_v, best_score = v, score
            self.total_choose_time += time.perf_counter() - t0
            return best_v

        discovery = {}
        low = {}
        parent = {}
        time_stamp = 0
        cut_nodes_impact = {v: 0 for v in active}
        visited = set()

        def dfs_tarjan(u):
            nonlocal time_stamp
            discovery[u] = low[u] = time_stamp
            time_stamp += 1
            visited.add(u)
            children = 0
            for w in adj.get(u, ()):
                if w not in active:
                    continue
                if w not in visited:
                    parent[w] = u
                    children += 1
                    dfs_tarjan(w)
                    low[u] = min(low[u], low[w])
                    if u not in parent and children > 1:
                        cut_nodes_impact[u] = children - 1
                    if u in parent and low[w] >= discovery[u]:
                        cut_nodes_impact[u] += 1
                elif w != parent.get(u):
                    low[u] = min(low[u], discovery[w])

        base_components = 0
        for node in active:
            if node not in visited:
                base_components += 1
                dfs_tarjan(node)

        for v in active:
            degree = len(adj.get(v, ()))
            activity_score = self.activity[v] / maxact
            comp = base_components + cut_nodes_impact[v]
            separation = min(
                1.0, max(0, comp - 1) / max(1, len(active) - 1)
            )
            influence = degree / maxdeg
            p, n = self.init_pos[v], self.init_neg[v]
            polarity_balance = 1.0 - abs(p - n) / max(1, p + n)
            structural = (
                0.60 * separation + 0.25 * influence
                + 0.15 * polarity_balance
            )
            cost = degree / max(1, len(active) - 1)
            score = activity_score + 0.35 * structural - 0.10 * cost
            if score > best_score:
                best_v, best_score = v, score

        self.total_choose_time += time.perf_counter() - t0
        return best_v

    def _search(self) -> bool:
        self.nodes += 1
        local_trail: List[Tuple[int, List[int], List[int]]] = []

        if not self._propagate(local_trail):
            for state in reversed(local_trail):
                self._unassign(state)
            return False

        v = self._choose()
        if v is None:
            return True

        self.decisions += 1
        preferred = True if self.polarity[v] >= 0 else False

        for val in (preferred, not preferred):
            branch_trail: List[Tuple[int, List[int], List[int]]] = []
            self._assign(v, val, branch_trail)
            if self._search():
                return True
            for state in reversed(branch_trail):
                self._unassign(state)

        self.activity[v] += 0.5
        for state in reversed(local_trail):
            self._unassign(state)
        return False

    def solve(self) -> Tuple[bool, Dict[int, bool], dict]:
        self.start_time = time.perf_counter()
        sat = self._search()
        elapsed = time.perf_counter() - self.start_time
        model = {
            i: self.assignment.get(i, False)
            for i in range(1, self.nvars + 1)
        }
        stats = {
            "decisions": self.decisions,
            "nodes": self.nodes,
            "conflicts": self.conflicts,
            "time_total_sec": elapsed,
            "time_choose_sec": self.total_choose_time,
            "time_propagate_sec": self.total_propagate_time,
            "heuristic": self.heuristic,
        }
        return sat, model, stats


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("input", help="archivo CNF DIMACS")
    ap.add_argument(
        "--heuristic", choices=["mistar", "activity"], default="mistar"
    )
    args = ap.parse_args()

    try:
        cnf = parse_dimacs(args.input)
        solver = MIStarSolverIncremental(cnf, heuristic=args.heuristic)
        sat, _, stats = solver.solve()
        print(f"s {'SATISFIABLE' if sat else 'UNSATISFIABLE'}")
        print("c stats " + " ".join(f"{k}={v}" for k, v in stats.items()))
        return 10 if sat else 20
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
