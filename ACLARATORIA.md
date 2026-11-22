# Nota Aclaratoria y Guía de Lectura del Corpus IGLV
# Methodological Note & Reading Guide for the IGLV Corpus (ES / EN)

---

## 🇪🇸 Versión en Español — Guía Metodológica y Conceptual

El **Corpus IGLV** (desarrollado por **Ignacio López Villanueva**) establece una arquitectura de ingeniería ontológica, viabilidad sistémica y coherencia estructural, articulando una base bilingüe (`ES / EN`) que orienta tanto la conceptualización como la implementación computacional.

### 1. Epistemología: Verdad contextual frente a Popper
* **Principio G:** Frente al falsacionismo clásico que busca una verdad absoluta externa, define la validez como **viabilidad operativa** dentro de un régimen específico (**Contexto 1.0**). Al mutar las condiciones (**Contexto 2.0**), el modelo requiere una nueva formulación adaptativa.
* **Evolución de paradigmas en ciencia:** Se ilustra mediante el paso histórico desde el *fluido calórico* de Carnot hasta la mecánica estadística de Boltzmann y el principio de Landauer sobre el coste de borrado de información, demostrando cómo el significado operativo de un fenómeno físico cambia según la resolución de medida.
* **En palabras del autor:** *"La validez de una explicación depende de su contexto. Si ampliamos el contexto, puede variar la solución y/o su dominio de validez; como en el caso del fuego, cuyo valor explicativo ha ido cambiando a medida que descubrimos más exterior."*

### 2. Metamatemática: Infinito interior y *Operium* frente a Gödel
* **Cierre arquitectónico:** Frente a las limitaciones de los sistemas axiomáticos estáticos descritas por Gödel, el modelo acota un **infinito interior** con resolución operativa pendiente ([DOI: 10.5281/zenodo.20916867](https://doi.org)).
* **Cascada de Extracción:** A través de *El Operium* ([DOI: 10.5281/zenodo.24302409](https://doi.org)), un operador base extrae nuevas estructuras de un campo continuo mediante procesos de `_metacierre`, transformando la incompletitud en capacidad adaptativa continua.
* **En palabras del autor:** *"Se deduce de la teoría de Ignición que la expansión resultante es hacia el interior. Un sistema acotado contiene más estructura de la que su propia resolución actual permite desplegar: su frontera externa es finita, pero su profundidad interna es inagotable mediante exploración dinámica."*

### 3. Complejidad Computacional: $P \neq NP$ como ley de diseño
* **Asimetría estructural:** Se asume que la búsqueda o **descubrimiento** en un espacio desordenado es intratable, mientras que la **verificación** sobre estructuras ordenadas resulta eficiente.
* **Tratabilidad por diseño:** Los sistemas organizan su espacio de estados mediante reducción de fricción y descomposición incremental (como se ejemplifica en `MI*-SAT v0.3`, [DOI: 10.5281/zenodo.23881112](https://doi.org)) en lugar de recurrir a la fuerza bruta.
* **En palabras del autor:** *"P es distinto de NP: verificar no es descubrir. La transición hacia un régimen tratable ocurre cuando la propia estructura descubierta reorganiza el espacio de búsqueda, permitiendo que el sistema opere a partir de ahí con el coste eficiente de una verificación."*

### 4. Estratificación y Ecosistema
* **Tres estratos de desarrollo (`Ignición`):**
  1. *Nivel 1 (Génesis y Extracción):* Marco teórico base ([DOI: 10.5281/zenodo.21670117](https://doi.org)) y *El Operium* ([DOI: 10.5281/zenodo.24302409](https://doi.org)).
  2. *Nivel 2 (Arquitectura e Invariantes):* Iteraciones de código `v1–v7` ([DOI: 10.5281/zenodo.23852880](https://doi.org)).
  3. *Nivel 3 (Dinámica Disipativa):* *Motor Ignición* `v3–v5` sin subsidio externo ([DOI: 10.5281/zenodo.23911868](https://doi.org)).
* **Difusión y lenguas:** Gestionado a través de GitHub (edición canónica bilingüe `ES / EN`), Zenodo (bóveda certificada con textos originales en gallego, español e inglés, incluyendo la comunidad `corpus-ignaciano`) y PhilPapers / PhilArchive.

---

## 🇬🇧 English Version — Methodological & Conceptual Guide

The **IGLV Corpus** (developed by **Ignacio López Villanueva**) establishes an architecture for ontological engineering, systemic viability, and structural coherence, providing a bilingual (`ES / EN`) foundation that guides both formal conceptualization and computational implementation.

### 1. Epistemology: Contextual Truth vs. Popper
* **Principle G:** Against classical falsificationism seeking a static external truth, validity is defined as **operational viability** within a specific regime (**Context 1.0**). When boundary conditions shift (**Context 2.0**), the model requires an adaptive reformulation.
* **Paradigm shifts in science:** Illustrated by the historical progression from Carnot's *caloric fluid* to Boltzmann's statistical mechanics and Landauer's principle on the thermodynamic cost of information erasure, showing how the operational meaning of a physical phenomenon changes with measurement resolution.
* **In the author's words:** *"The validity of an explanation depends on its context. As we expand the context, the solution and its domain of validity shift—much like fire, whose explanatory value has transformed as we uncovered more of the external world."*

### 2. Metamathematics: Internal Infinity & *Operium* vs. Gödel
* **Architectural closure:** Against the static limitations of formal axiomatic systems described by Gödel, the model bounds an **internal infinity** with pending operational resolution ([DOI: 10.5281/zenodo.20916867](https://doi.org)).
* **Extraction Cascade:** Through *The Operium* ([DOI: 10.5281/zenodo.24302409](https://doi.org)), a base operator extracts new structures from a continuous field via `_metaclosure` processes, turning formal incompleteness into continuous adaptive capacity.
* **In the author's words:** *"It follows from Ignition theory that the resulting expansion moves inward. A bounded system contains more structure than its current resolution can unfold: its outer boundary is finite, yet its internal depth is inexhaustible through dynamic exploration."*

### 3. Computational Complexity: $P \neq NP$ as a Design Law
* **Structural asymmetry:** Search or **discovery** in an unstructured space is assumed intractable, whereas **verification** over ordered structures is efficient.
* **Tractability by design:** Capable systems organize their state space through friction reduction and incremental graph decomposition (as exemplified in `MI*-SAT v0.3`, [DOI: 10.5281/zenodo.23881112](https://doi.org)) rather than brute-force search.
* **In the author's words:** *"P is distinct from NP: verifying is not discovering. The transition toward a tractable regime occurs when the discovered structure itself reorganizes the search space, allowing the system to operate thereafter at the efficient cost of verification."*

### 4. Stratification & Ecosystem
* **Three development layers (`Ignition`):**
  1. *Layer 1 (Genesis & Extraction):* Base theoretical framework ([DOI: 10.5281/zenodo.21670117](https://doi.org)) and *The Operium* ([DOI: 10.5281/zenodo.24302409](https://doi.org)).
  2. *Layer 2 (Architecture & Invariants):* Code iterations `v1–v7` ([DOI: 10.5281/zenodo.23852880](https://doi.org)).
  3. *Layer 3 (Dissipative Dynamics):* *Ignition Engine* `v3–v5` without external subsidy ([DOI: 10.5281/zenodo.23911868](https://doi.org)).
* **Dissemination & languages:** Managed across GitHub (curated bilingual `ES / EN` canonical edition), Zenodo (DOI-certified vault hosting original texts in Galician, Spanish, and English, including the `corpus-ignaciano` community), and PhilPapers / PhilArchive.

