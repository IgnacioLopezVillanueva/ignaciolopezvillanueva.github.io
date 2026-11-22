# Nota Aclaratoria y Guía de Lectura del Corpus IGLV
# Methodological Note & Reading Guide for the IGLV Corpus (ES / EN)

---

## 🇪🇸 Versión en Español — Cómo leer este Corpus (Puente Conceptual y Técnico)

El **Corpus IGLV** es una arquitectura cerrada de ingeniería ontológica, sistemas abiertos y viabilidad operativa desarrollada por **Ignacio López Villanueva**. Para evitar malentendidos habituales al trasladar términos de la filosofía clásica, la lógica matemática o la teoría de la complejidad al diseño de sistemas capaces, esta nota fija explícitamente las reglas de lectura del repositorio:

### 1. Epistemología: Verdad contextual (*Principio G*) frente al falsacionismo estático (Popper)
* **Qué plantea la epistemología clásica:** Se asume una verdad externa única e inamovible a la que las teorías se aproximan por refutación en un mismo tablero fijo.
* **Qué plantea el Corpus IGLV:** El **Principio G** no hace epistemología descriptiva estática, sino ingeniería de supervivencia sistémica. Un modelo o regla de acción es *operativamente verdadero* dentro de un régimen de resolución determinado (**Contexto 1.0**) en la medida en que permite al sistema mantener su cohesión frente a la entropía. Cuando cambia la escala o el entorno (**Contexto 2.0**), esa verdad contextual queda superada y exige extraer una nueva formulación.
* **Ejemplo histórico en ciencia dura:** En termodinámica del siglo XIX, la teoría del *fluido calórico* permitió a Sadi Carnot deducir el teorema de eficiencia máxima de los motores térmicos que sigue vigente hoy; al aumentar la resolución experimental, el calor pasó a definirse como agitación estadística molecular (Boltzmann) y, posteriormente, como coste energético de borrado de información (Landauer). El fenómeno persistió, pero su significado operativo mutó al cambiar de régimen.

### 2. Metamatemática: Cierre arquitectónico e infinito interior frente a Gödel
* **Qué demuestra Gödel:** Todo sistema formal axiomático estático lo suficientemente expresivo como para contener la aritmética es necesariamente incompleto si es consistente.
* **Qué plantea el Corpus IGLV:** La clausura anunciada en mayo de 2026 es un **cierre arquitectónico y de diseño** (fijar las reglas mínimas del motor para que no mute arbitrariamente), no una pretensión de completitud sintáctica gödeliana. Como se formaliza en *Invariancia Estructural y Lectura Generativa del Límite de Gödel* (`DOI: 10.5281/zenodo.20916867`) y en *El Operium y la Cascada de Extracción* (`DOI: 10.5281/zenodo.24302409`), una acotación cerrada contiene un **infinito interior con resolución pendiente de desplegar**: al dotar al sistema de dinámica exploradora interna, el residuo no demostrado deja de ser un muro paralizante y se convierte en reserva continua de novedad estructural.

### 3. Complejidad Computacional: $P \neq NP$ como condición de diseño (*Descubrir vs. Verificar*)
* **El punto de partida:** Se asume la asimetría fundamental **$P \neq NP$**: **descubrir** una solución en un espacio arbitrario sin estructura es combinatoriamente costoso, mientras que **verificar** una estructura ya ordenada es eficiente.
* **Qué plantea el Corpus IGLV:** El corpus no pretende resolver instancias arbitrarias del peor caso por fuerza bruta, sino formular una **ley de diseño arquitectónico**. Un sistema viable sobrevive porque organiza su espacio de representación (acotando su *treewidth*, reduciendo la fricción $R$ en el *Sistema Cian* o aplicando análisis estructural incremental como en `MI*-SAT v0.3`, `DOI: 10.5281/zenodo.23881112`) para operar en la región donde la tratabilidad estructural está garantizada.

### 4. Relación entre plataformas (GitHub, Zenodo y PhilPapers)
* **GitHub (`ignaciolopezvillanueva.github.io`):** Edición canónica curada, bilingüe (`ES / EN`), con la especificación consolidada y el código reproducible.
* **Zenodo (Bóveda certificada con DOI):** Archivo cronológico inmutable con todos los registros formales, incluyendo la comunidad específica del Sistema Cian (`corpus-ignaciano`).
* **PhilPapers / PhilArchive:** Archivo abierto de evolución, ensayos exploratorios y difusión filosófica.

---

## 🇬🇧 English Version — How to Read This Corpus (Conceptual & Technical Bridge)

The **IGLV Corpus** is a closed architecture for ontological engineering, open systems, and operational viability developed by **Ignacio López Villanueva**. To prevent common misinterpretations when mapping terms from classical philosophy, mathematical logic, or computational complexity onto capable systems engineering, this note defines the explicit reading rules of the repository:

### 1. Epistemology: Contextual Truth (*Principle G*) vs. Static Falsificationism (Popper)
* **Classical framing:** Assumes a single, immovable external truth approached asymptotically on a fixed board.
* **IGLV Corpus framing:** **Principle G** addresses systemic viability engineering rather than static descriptive epistemology. A model or action rule is *operationally true* within a given resolution regime (**Context 1.0**) insofar as it preserves system cohesion against entropy. When resolution or environmental conditions shift (**Context 2.0**), that contextual truth is superseded and requires extracting a new operational formulation.
* **Hard-science illustration:** In 19th-century thermodynamics, the *caloric fluid* model enabled Sadi Carnot to derive the maximum thermal efficiency theorem still valid today; as experimental resolution increased, heat was redefined as statistical molecular motion (Boltzmann) and later as the energetic cost of information erasure (Landauer). The physical phenomenon persisted while its operational definition shifted across regimes.

### 2. Metamathematics: Architectural Closure & Internal Infinity vs. Gödel
* **Gödel's result:** Any static, consistent formal axiomatic system expressive enough for basic arithmetic is necessarily incomplete.
* **IGLV Corpus framing:** The formal closure established in May 2026 denotes **architectural and design closure** (freezing minimal control invariants so the engine does not drift arbitrarily), not Gödelian syntactic completeness. As formalized in *Structural Invariance and Generative Reading of Gödel's Limit* (`DOI: 10.5281/zenodo.20916867`) and *Operium and the Extraction Cascade* (`DOI: 10.5281/zenodo.24302409`), a bounded architecture contains an **unexhausted internal infinity**: equipping the system with dynamic internal exploration turns formal incompleteness from a static barrier into a continuous gradient of structural extraction.

### 3. Computational Complexity: $P \neq NP$ as a Design Condition (*Discovery vs. Verification*)
* **Baseline:** The corpus starts from the fundamental asymmetry **$P \neq NP$**: **discovering** a solution in an unstructured adversarial space is combinatorially hard, whereas **verifying** an ordered structure is efficient.
* **IGLV Corpus framing:** Rather than claiming a brute-force solution to worst-case instances, the corpus formulates an **architectural design condition**. A viable system survives by structuring its state space—bounding treewidth, minimizing friction $R$ within the *Cyan System*, or applying incremental structural decomposition as implemented in `MI*-SAT v0.3` (`DOI: 10.5281/zenodo.23881112`)—to remain within structurally tractable regimes.

### 4. Ecosystem Role Separation (GitHub, Zenodo, and PhilPapers)
* **GitHub (`ignaciolopezvillanueva.github.io`):** Curated, bilingual (`ES / EN`) canonical edition containing consolidated specifications and reproducible code.
* **Zenodo (DOI-certified vault):** Immutable chronological archive containing all formal records, including the dedicated Cyan System community (`corpus-ignaciano`).
* **PhilPapers / PhilArchive:** Open exploratory archive tracking conceptual evolution and philosophical dissemination.
