#!/usr/bin/env python3
"""
Corpus IGLV: Especificación Formal del Motor Ignición v5
Implementación de referencia — Viabilidad estocástica acotada bajo choques exponenciales
Autor: Ignacio López Villanueva (ORCID: 0009-0008-4817-5228)
Referencia: DOI 10.5281/zenodo.23911868
Licencia: CC BY-NC 4.0
"""

from collections import Counter
import numpy as np


class MotorIgnicionV5Riguroso:
    def __init__(
        self,
        rho=0.5,
        eta=0.65,
        c_tope=115.0,
        omega_irr=126.64,
        r_target=100.0,
        r_critico=20.0,
        k_max=200.0,
        c_op=5.0,
        k0=80.0,
    ):
        self.rho, self.eta, self.c_tope, self.omega_irr = (
            rho,
            eta,
            c_tope,
            omega_irr,
        )
        self.R_target, self.R_critico, self.K_max, self.c_op = (
            r_target,
            r_critico,
            k_max,
            c_op,
        )
        self.R = r_target
        self.K = k0
        self.tiempo_absorcion = None
        self.estado_ruina = None

    def paso_discreto(self, choque, t):
        if self.estado_ruina is not None:
            return
        if choque >= self.omega_irr:
            self.R = 0.0
            self.estado_ruina = "CHOQUE_FATAL"
            self.tiempo_absorcion = t
            return

        d = self.rho * (self.R / self.R_target)
        abs_t = d * min(choque, self.c_tope)
        pan_t = self.eta * abs_t * max(0.0, 1.0 - choque / self.omega_irr)
        r_prel = self.R - self.c_op + pan_t

        if r_prel > self.R_target:
            self.K = min(self.K_max, self.K + (r_prel - self.R_target))
            self.R = self.R_target
        else:
            deficit = self.R_target - r_prel
            if self.K >= deficit:
                self.K -= deficit
                self.R = self.R_target
            else:
                self.R = r_prel + self.K
                self.K = 0.0

        if self.R <= self.R_critico:
            self.estado_ruina = "INANICION"
            self.tiempo_absorcion = t


def simular(N=10000, T=1000, beta=30.0, seed=42, **kw):
    np.random.seed(seed)
    tau = np.full(N, np.inf)  # tau = t + 1 (pasos completados hasta absorcion)
    causa = []
    for i in range(N):
        m = MotorIgnicionV5Riguroso(**kw)
        for t in range(T):
            m.paso_discreto(np.random.exponential(scale=beta), t)
            if m.estado_ruina is not None:
                tau[i] = t + 1
                causa.append(m.estado_ruina)
                break
    return tau, causa


if __name__ == "__main__":
    N, T = 10000, 1000
    tau, causa = simular(N, T)
    surv = np.isinf(tau).sum()
    ab = tau[np.isfinite(tau)]
    print("supervivientes", surv, "S(T)=", surv / N)
    print(
        "T_m (t+1)",
        ab.mean(),
        "(indice 0-based:",
        (ab - 1).mean(),
        ") sd",
        ab.std(ddof=1),
        "SE",
        ab.std(ddof=1) / np.sqrt(len(ab)),
    )
    print(Counter(causa))
    for t in (10, 50, 100, 200, 500, 1000):
        print("S(%d)=%.4f" % (t, np.mean(tau > t)))
