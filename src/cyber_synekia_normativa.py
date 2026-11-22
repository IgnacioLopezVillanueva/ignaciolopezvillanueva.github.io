#!/usr/bin/env python3
"""
Cyber-Synekia: Tratado de Persistencia Relacional y Máquina de Persistencia
Módulo de Verificación Computacional del Convenio Dinámico
Autor: Ignacio López Villanueva (ORCID: 0009-0008-4817-5228)
Referencia: DOI 10.5281/zenodo.23853133
Fecha de Compilación: 17 de Octubre de 2026
"""

import random


class RadarConvenio:
    def __init__(self, num_vertices):
        self.N = num_vertices
        self.limite_puentes_criticos = 3

    def calcular_componentes_conexos(self, grafo):
        """
        Evalúa por Búsqueda en Anchura (BFS) la conectividad del sistema.
        Actúa como el operador lógico del Convenio para verificar la
        característica constitutiva de comunicación global.
        """
        visitados = set()
        componentes = 0
        for nodo in range(self.N):
            if nodo not in visitados:
                componentes += 1
                queue = [nodo]
                visitados.add(nodo)
                while queue:
                    actual = queue.pop(0)
                    for vecino in grafo.get(actual, set()):
                        if vecino not in visitados:
                            visitados.add(vecino)
                            queue.append(vecino)
        return componentes

    def obtener_todas_aristas(self, grafo):
        """Extrae el conjunto único de aristas activas en el sistema."""
        aristas = set()
        for u in grafo:
            for v in grafo[u]:
                if u < v:
                    aristas.add((u, v))
        return aristas

    def evaluar_distancia_ruptura(self, grafo):
        """
        Calcula cuántas aristas actúan como puentes críticos en el instante t.
        Una arista es un puente si su eliminación rompe la conectividad global,
        incrementando el número de componentes conexos aislados.
        """
        comp_originales = self.calcular_componentes_conexos(grafo)
        aristas = self.obtener_todas_aristas(grafo)
        puentes = 0
        for u, v in aristas:
            # Simular de forma temporal la eliminación de la arista en la red
            grafo[u].remove(v)
            grafo[v].remove(u)
            nuevos_comp = self.calcular_componentes_conexos(grafo)
            if nuevos_comp > comp_originales:
                puentes += 1
            # Restaurar la arista para mantener la integridad del estado actual
            grafo[u].add(v)
            grafo[v].add(u)
        return puentes

    def evaluar_sistema(self, grafo):
        """
        Juzga el estado actual frente al Convenio de forma binaria (I_t).
        Retorna: (Identidad_Binaria, Distancia_Ruptura, Color_Semaforo)
        """
        componentes = self.calcular_componentes_conexos(grafo)
        # Restricción constitutiva dura: Conectividad Total (Componentes = 1)
        if componentes > 1 or len(self.obtener_todas_aristas(grafo)) == 0:
            return 0, 0, "ROJO (Extinción Ontológica: Modo Museo)"
        distancia = self.evaluar_distancia_ruptura(grafo)
        if distancia <= self.limite_puentes_criticos:
            return 1, distancia, "ÁMBAR (Riesgo Estructural: Alerta al Entrenador)"
        return 1, distancia, "VERDE (Identidad Conforme al Convenio)"


class SimuladorDinamicaC:
    def __init__(self, num_vertices):
        self.N = num_vertices
        # Inicializar como Grafo Completo K_N para garantizar el cumplimiento del Convenio
        self.grafo = {i: set() for i in range(self.N)}
        for i in range(self.N):
            for j in range(i + 1, self.N):
                self.grafo[i].add(j)
                self.grafo[j].add(i)

    def ejecutar_ciclo_mutacion(self, tasa_degradacion, tasa_reparacion):
        """
        Simula el Lazo de Transformación de la Continuidad Histórica.
        Introduce degradación aleatoria (caos) del entorno y reconexión gradual.
        """
        aristas = list(RadarConvenio(self.N).obtener_todas_aristas(self.grafo))
        # Fase de Degradación: El entorno altera y destruye relaciones materiales
        for _ in range(min(tasa_degradacion, len(aristas))):
            if not aristas:
                break
            u, v = random.choice(aristas)
            if v in self.grafo[u]:
                self.grafo[u].remove(v)
            if u in self.grafo[v]:
                self.grafo[v].remove(u)
            aristas.remove((u, v))
        # Fase de Reparación Gradual (Continuidad): Reconexión estocástica aleatoria
        for _ in range(tasa_reparacion):
            u = random.randint(0, self.N - 1)
            v = random.randint(0, self.N - 1)
            if u != v:
                self.grafo[u].add(v)
                self.grafo[v].add(u)


# --- BLOQUE EJECUTABLE DE VERIFICACIÓN ---
if __name__ == "__main__":
    random.seed(42)  # Semilla inmutable para reproducibilidad absoluta
    vertices = 10
    simulador = SimuladorDinamicaC(vertices)
    radar = RadarConvenio(vertices)

    print("=== INICIANDO SIMULACIÓN DE CYBER-SYNEKIA ===")
    print(f"Sistema inicializado con {vertices} vértices en conectividad plena.")

    # Simular evolución continua a lo largo de ciclos causales ininterrumpidos
    for ciclo in range(1, 16):
        degradacion = 3 + (ciclo // 3)
        reparacion = 1
        simulador.ejecutar_ciclo_mutacion(
            tasa_degradacion=degradacion, tasa_reparacion=reparacion
        )
        aristas_vivas = len(radar.obtener_todas_aristas(simulador.grafo))
        identidad, distancia, semaforo = radar.evaluar_sistema(simulador.grafo)

        print(f"\n[Ciclo {ciclo:02d}] Continuidad Histórica: ACTIVA (Aristas: {aristas_vivas})")
        print(f"  Evaluación del Convenio -> Identidad Binaria: {identidad}")
        print(f"  Distancia a la Ruptura: {distancia} puentes")
        print(f"  Estado del Semáforo   : {semaforo}")

        if identidad == 0:
            print("!!! MUTACIÓN DETECTADA: La continuidad sigue, pero la identidad ha muerto.")
            break
