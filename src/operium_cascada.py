#!/usr/bin/env python3
"""
El Operium y la Cascada de Extracción
Arquitectura viva del Motor Ignición V5 y demostración computacional en Python
Operium = P1 + C1 = P1 + P2 + C2 = P1 + P2 + P3 + C3 = ...
Autor: Ignacio López Villanueva (ORCID: 0009-0008-4817-5228)
Referencia: DOI 10.5281/zenodo.24302409
Licencia: CC BY-NC 4.0
"""

import numpy as np

# Constantes operativas de ventana, asimilación y banda segura
ETA = 0.15       # Tasa de actualización de estado ante impacto C1
N_WIN = 10       # Ventana de memoria reciente de fricción
LAM_LO = 0.20    # Cota inferior del espectro reconfigurado (P2)
LAM_HI = 0.95    # Cota superior del espectro reconfigurado (P2)
Q_KEEP = 3       # Fracción de memoria retenida como residuo vivo (C2)


class Motor:
    """Operador activo P1 que confronta impactos C1 y muta hacia P2 dejando residuo C2."""

    def __init__(self, dim: int = 4, theta: float = 2.5):
        self.dim = dim
        self.theta = theta
        self.A = np.eye(dim) * 0.5   # Matriz de respuesta interna
        self.x = np.zeros(dim)       # Estado operativo
        self.hist = []               # Historial reciente de fricción
        self.mutaciones_p2 = 0       # Contador de disparos de _metacierre

    def step(self, c: np.ndarray) -> float:
        # C1 (impacto externo) confronta la respuesta operativa actual
        e = c - self.A @ self.x
        self.x = self.x + ETA * e
        G = np.outer(e, e)

        # Se acumula la memoria reciente de fricción en la ventana N_WIN
        self.hist.append(G)
        if len(self.hist) > N_WIN:
            self.hist.pop(0)

        # Presión operativa acumulada sobre el historial vigente
        R = sum(self.hist)
        press = float(np.linalg.norm(R))

        # Si la presión supera el umbral, el motor reconfigura su respuesta (P2)
        if self.theta is not None and press > self.theta:
            self._metacierre(R)

        return press

    def _metacierre(self, R: np.ndarray) -> None:
        # Análisis de los ejes principales de tensión en el residuo acumulado R
        w, Qm = np.linalg.eigh(R)
        sig = w[::-1]
        Qm = Qm[:, ::-1]

        # Reconfiguración de la respuesta estructural (P2) dentro de banda segura
        denom = sig[0] if sig[0] > 1e-12 else 1.0
        lam = LAM_LO + (LAM_HI - LAM_LO) * sig / denom
        self.A = Qm @ np.diag(lam) @ Qm.T

        # Depuración parcial de la memoria (representación computacional de C2)
        self.hist = self.hist[-Q_KEEP:]
        self.mutaciones_p2 += 1


if __name__ == "__main__":
    rng = np.random.default_rng(42)
    motor = Motor(dim=4, theta=2.5)
    print("=== CASCADA DE EXTRACCIÓN DEL OPERIUM (P1 + C1 -> P1 + P2 + C2) ===")
    for t in range(1, 51):
        c_t = rng.normal(0.0, 0.85, size=4)
        press = motor.step(c_t)
        if t % 10 == 0:
            print(
                f"[Ciclo {t:02d}] Presión={press:.4f} | "
                f"Mutaciones P2={motor.mutaciones_p2} | "
                f"Residuo vivo C2={len(motor.hist)}"
            )
