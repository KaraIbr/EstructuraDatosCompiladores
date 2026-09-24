# Apunte — Unidad 2 · Métodos de Ordenación

Apunte de estudio para **Estructuras de Datos y Compiladores** (Séptimo cuatrimestre), reconstruido a partir de los apuntes de clase de la **GLOBAL UNIVERSITY (Dra. Blanca Guadalupe Estrada Renteria)**, basados en el **Capítulo 8 de Oswaldo Cairo, *Estructura de Datos* (3.ª ed.)**.

Cada método incluye, en el mismo orden que los apuntes: **en palabras (analogía) · cómo se ejecuta · algoritmo del libro · ejemplo trabajado · ejercicios para el estudiante · notas de memoria/eficiencia**.

---

## Tabla de contenido

- Propósito y alcance: ordenación interna vs. externa
- Características del ordenamiento (estabilidad, adaptabilidad, tiempo, espacio)
- **Ordenación interna — métodos directos**
  1. Intercambio directo (burbuja)
  2. Intercambio directo con señal
  3. Sacudida (Shaker Sort)
  4. Inserción directa
  5. Selección directa
  6. Análisis de eficiencia de los métodos directos
- **Ordenación interna — métodos logarítmicos**
  7. Shell
  8. Quicksort
  9. Heapsort (montículo)
- **Ordenación externa e intercalación de archivos**
  10. Ordenación externa e intercalación de archivos
  11. Ordenación de archivos
  12. Ordenación por mezcla directa
  13. Ordenación por mezcla equilibrada
- Síntesis final
- Anexo A · Recursos visuales
- Anexo B · Soluciones de los ejercicios
- Anexo C · Regla de oro para exámenes

---

## Propósito y alcance de las ordenaciones

Ordenar significa **reorganizar un conjunto de datos en una secuencia específica** (ascendente o descendente). El capítulo 8 de Cairo clasifica los métodos según **dónde están los datos**:

- **Ordenación interna:** los elementos están en **memoria principal**; se trabaja con **arreglos unidimensionales**.
- **Ordenación externa:** los datos no caben en memoria principal y se encuentran en **archivos de almacenamiento secundario**; se trabaja directamente con archivos.

A su vez, la ordenación interna se divide en:

| Grupo | Característica |
|---|---|
| **Métodos directos** | Implementación sencilla, pero ineficientes cuando N es mediano o grande. |
| **Métodos logarítmicos** | Más complejos, pero con menor número de comparaciones y movimientos (O(n log n)). |

> Los métodos externos principales según la fuente son **mezcla directa** y **mezcla equilibrada**.

### Sobre la eficiencia (Wirth, Kernighan)

- La eficiencia se determina por el **equilibrio entre tiempo de ejecución y uso de memoria** (Niklaus Wirth, *Algorithms + Data Structures = Programs*), considerando siempre la **simplicidad y claridad** del diseño.
- Un algoritmo eficiente no solo debe ser rápido, sino **claro, mantenible y apropiado al contexto** (Brian Kernighan, *The Practice of Programming*).
- **No siempre el algoritmo más rápido es el más conveniente:** a veces se sacrifica tiempo para ahorrar memoria, o viceversa.
- Al elegir un algoritmo en ingeniería se evalúa: **tamaño del conjunto de datos, recursos del sistema, necesidad de estabilidad y escalabilidad futura.**

---

## Características del ordenamiento

Un algoritmo de ordenamiento es un **procedimiento sistemático que reorganiza los elementos según una relación de orden definida** (Horowitz y Sahni, *Fundamentals of Data Structures*). Las características que determinan su comportamiento práctico (Sedgewick, *Algorithms*):

### 1. Estabilidad

Un algoritmo de ordenamiento es **estable** si **mantiene el orden relativo de los elementos que poseen claves iguales**.

> Según Cormen (*Introduction to Algorithms*), la estabilidad es crucial cuando los registros tienen **múltiples campos** y se ordena por una clave secundaria.

**Ejemplo:** lista de estudiantes ordenada primero por matrícula y luego por promedio. Si el algoritmo es estable, los estudiantes con el mismo promedio conservan el orden original de matrícula.

- **MergeSort es estable**
- **QuickSort tradicional no es estable**

### 2. Adaptabilidad

Un algoritmo es **adaptativo** si **mejora su desempeño cuando los datos están parcialmente ordenados** (Knuth, *The Art of Computer Programming*).

- **Inserción directa** puede llegar a O(n) cuando los datos están casi ordenados.
- **Selección directa** mantiene O(n²) sin importar el orden inicial.
- El conocimiento previo sobre los datos influye directamente en la elección del algoritmo.

### 3. Complejidad temporal

Es la **tasa de crecimiento del número de operaciones** en función del tamaño de la entrada; se expresa con notación asintótica **Big-O**.

- Para conjuntos pequeños, O(n²) puede ser aceptable.
- Para grandes volúmenes, solo los algoritmos **O(n log n)** resultan viables (la diferencia se vuelve crítica cuando n crece).

### 4. Complejidad espacial

Es la **cantidad de memoria adicional** que requiere el algoritmo. Un algoritmo es **in-place** cuando ordena sin usar memoria adicional significativa.

- En sistemas con restricciones de memoria, esta característica es determinante.

> Dos algoritmos pueden ordenar correctamente el mismo arreglo y diferir dramáticamente en comparaciones, intercambios, consumo de memoria o comportamiento ante datos parcialmente ordenados.

---

# ORDENACIÓN INTERNA · MÉTODOS DIRECTOS

---

## 1. Ordenación por intercambio directo (burbuja)

### 🗣️ En palabras

**Analogía:** como las burbujas de aire que suben en un vaso de agua, cada pasada "flota" un elemento hasta su lugar: o el **más pequeño sube a la izquierda**, o el **más grande baja a la derecha**.

**Descripción directa:** compara **pares de elementos adyacentes** y los intercambia cuando están en orden incorrecto. Puede ejecutarse en dos variantes. En total se realizan **n − 1 pasadas** hasta colocar todos los elementos.

### 📋 Cómo se ejecuta (dos variantes)

1. **Variante menor a la izquierda:** recorrer de derecha a izquierda, comparar `A[J−1]` con `A[J]` e intercambiar si el primero es mayor. Cada pasada fija un nuevo elemento pequeño en el extremo izquierdo.
2. **Variante mayor a la derecha:** recorrer de izquierda a derecha, comparar `A[J]` con `A[J+1]` e intercambiar si el primero es mayor. Cada pasada fija un nuevo elemento grande en el extremo derecho.

### 📘 Algoritmos del libro

**Algoritmo 8.1 · Burbuja_menor (transporta el menor a la izquierda)**
```
Variables: I, J, AUX enteros
1. Repetir con I desde 2 hasta N
   1.1 Repetir con J desde N hasta I (descendente)
       1.1.1 Si A[J−1] > A[J] entonces
                 AUX   ←  A[J−1]
                 A[J−1] ← A[J]
                 A[J]  ←  AUX
       {fin del condicional}
   {fin del ciclo}
{fin del ciclo}
```

**Algoritmo 8.2 · Burbuja_mayor (transporta el mayor a la derecha)**
```
Variables: I, J, AUX enteros
1. Repetir con I desde N−1 hasta 1
   1.1 Repetir con J desde 1 hasta I
       1.1.1 Si A[J] > A[J+1] entonces
                 AUX   ←  A[J]
                 A[J]  ←  A[J+1]
                 A[J+1] ← AUX
       {fin del condicional}
   {fin del ciclo}
{fin del ciclo}
```

### 🧮 Ejemplo del libro (8.1–8.2)

Arreglo inicial: `A = [15, 67, 08, 16, 44, 27, 12, 35]` con la variante **menor a la izquierda**. La primera pasada coloca 08 en la primera posición y la segunda coloca 12 en la segunda.

**Primera pasada reescrita (recorrido de derecha a izquierda):**

| Comparación | Resultado |
|---|---|
| 12 > 35 | No hay intercambio |
| 27 > 12 | Sí: 27 y 12 se intercambian |
| 44 > 12 | Sí: 44 y 12 se intercambian |
| 16 > 12 | Sí: 16 y 12 se intercambian |
| 08 > 12 | No hay intercambio |
| 67 > 08 | Sí: 67 y 08 se intercambian |
| 15 > 08 | Sí: 15 y 08 se intercambian |

| Estado | Arreglo |
|---|---|
| Inicial | 15 67 08 16 44 27 12 35 |
| 1.ª pasada | 08 15 67 12 16 44 27 35 |
| 2.ª pasada | 08 12 15 67 16 27 44 35 |
| Final | 08 12 15 16 27 35 44 67 |

### ✅ Ejercicios para el estudiante

1. Ordene `A = [42, 18, 35, 07, 26, 11]` transportando el menor hacia la izquierda. Muestre el arreglo al terminar cada pasada. *(solución en Anexo B)*
2. Ordene `A = [31, 12, 48, 09, 25, 17]` transportando el mayor hacia la derecha. Señale en cada pasada qué elemento queda definitivamente colocado. *(solución en Anexo B)*

### 💡 Notas y memoria/eficiencia

- Tiempo: **O(n²)** en promedio/peor; ~(n² − n)/2 comparaciones siempre (ver sección 6).
- Memoria: **O(1)** (in-place, solo usa `AUX`).
- Estable: **Sí** (intercambia solo adyacentes).
- En la práctica se usa como aprendizaje y para datos "casi ordenados" combinado con la señal (sección 2).

---

## 2. Ordenación por intercambio directo con señal

### 🗣️ En palabras

**Analogía:** es la burbuja "inteligente": antes de terminar de dar vueltas, verifica si en una pasada completa no se hizo **ningún intercambio**. Si eso pasa, el arreglo ya está ordenado y **puede parar**, sin gastar las n − 1 pasadas de más.

**Descripción directa:** usa una **marca o señal (bandera BAND)** para detectar si en una pasada no se produjo ningún intercambio. Si BAND permanece *VERDADERO* al terminar la pasada, el arreglo ya quedó ordenado y la ejecución termina de forma anticipada.

### 📋 Cómo se ejecuta

1. Inicializar `I` y la bandera `BAND`.
2. Al iniciar una pasada, **suponer que no habrá cambios**: `BAND ← VERDADERO`.
3. Comparar pares adyacentes; **cada vez que se intercambie**, poner `BAND ← FALSO`.
4. Si al terminar la pasada `BAND` permanece *VERDADERO*, detener el algoritmo; si no, realizar otra pasada.

### 📘 Algoritmo del libro

**Algoritmo 8.3 · Burbuja_señal**
```
Variables: I, J, AUX enteros; BAND booleana
1. Hacer I ← 1 y BAND ← FALSO
2. Mientras ((I ≠ N−1) y (BAND = FALSO)) repetir
   Hacer BAND ← VERDADERO
   2.1 Repetir con J desde 1 hasta N−1
       2.1.1 Si A[J] > A[J+1] entonces
                 AUX ← A[J]; A[J] ← A[J+1]; A[J+1] ← AUX
                 BAND ← FALSO
       {fin del condicional}
   {fin del ciclo}
   Hacer I ← I + 1
{fin del ciclo}
```

### 🧮 Aplicación didáctica de la regla de paro

Consideremos un arreglo **ya ordenado** `A = [08, 12, 15, 16, 27, 35, 44, 67]`:

| Estado de la pasada | BAND | Conclusión |
|---|---|---|
| Inicio de la pasada | VERDADERO | Se supone que el arreglo ya puede estar ordenado |
| No se produce ningún intercambio | Permanece VERDADERO | El ciclo termina de manera anticipada |

Al recorrer todos los pares adyacentes no ocurre ningún intercambio; `BAND` no cambia a *FALSO* y el algoritmo termina **después de esa única pasada**.

### ✅ Ejercicios para el estudiante

1. Aplique burbuja con señal a `A = [08, 12, 15, 27, 16, 35, 44]`. Indique en qué pasada se produce el último intercambio y en cuál se detiene. *(solución en Anexo B)*
2. Aplique el método a `A = [05, 10, 15, 20, 25]`. Registre `BAND` al inicio y al final de la primera pasada y explique por qué no se requieren n − 1 pasadas. *(solución en Anexo B)*

### 💡 Notas y memoria/eficiencia

- Igual que burbuja pero con mejor caso **O(n)** (una sola pasada verifica si ya está ordenado).
- Memoria O(1) · Estable: Sí.
- Es la versión "útil" de la burbuja para arreglos casi ordenados.

---

## 3. Ordenación por el método de la sacudida (Shaker Sort)

### 🗣️ En palabras

**Analogía:** imagina agitar una bolsa de fichas hacia un lado y luego hacia el otro. La sacudida alterna los **dos sentidos de recorrido**: una pasada empuja los pequeños a la izquierda y la siguiente empuja los grandes a la derecha, encogiéndose por ambos extremos a la vez.

**Descripción directa:** optimiza el intercambio directo **mezclando sus dos sentidos**. Cada pasada tiene **dos etapas**: la primera va de derecha a izquierda (desplaza los pequeños) y la segunda de izquierda a derecha (desplaza los grandes). En ambas se **conserva la posición del último intercambio (K)** para reducir el intervalo de trabajo en las pasadas siguientes.

### 📋 Cómo se ejecuta

1. Definir los extremos `IZQ` y `DER` del intervalo activo.
2. Recorrer de `DER` a `IZQ`; intercambiar adyacentes desordenados y guardar en `K` la **última posición de intercambio**.
3. Actualizar `IZQ = K + 1`.
4. Recorrer de `IZQ` a `DER` en sentido ascendente; intercambiar y actualizar `K`.
5. Actualizar `DER = K − 1` y repetir mientras `DER >= IZQ`.

### 📘 Algoritmo del libro

**Algoritmo 8.4 · Sacudida**
```
Variables: I, IZQ, DER, K, AUX enteros
1. Hacer IZQ ← 2, DER ← N y K ← N
2. Mientras (DER >= IZQ) repetir
   2.1 Repetir con I desde DER hasta IZQ {descendente}
       2.1.1 Si A[I−1] > A[I] entonces
                 AUX ← A[I−1]; A[I−1] ← A[I]; A[I] ← AUX
                 K ← I
       {fin del condicional}
   {fin del ciclo}
   Hacer IZQ ← K + 1
   2.3 Repetir con I desde IZQ hasta DER {ascendente}
       2.3.1 Si A[I−1] > A[I] entonces
                 AUX ← A[I−1]; A[I−1] ← A[I]; A[I] ← AUX
                 K ← I
       {fin del condicional}
   {fin del ciclo}
   Hacer DER ← K − 1
{fin del ciclo}
```

### 🧮 Ejemplo 8.3 del libro

Arreglo inicial: `A = [15, 67, 08, 16, 44, 27, 12, 35]`.

| Etapa | Arreglo resultante | Última posición de intercambio |
|---|---|---|
| Inicial | 15 67 08 16 44 27 12 35 | — |
| P1–E1 | 08 15 67 12 16 44 27 35 | 2 |
| P1–E2 | 08 15 12 16 44 27 35 67 | 8 |
| P2–E1 | 08 12 15 16 27 44 35 67 | 3 |
| P2–E2 | 08 12 15 16 27 35 44 67 | 7 |
| 3.ª pasada · 1.ª etapa | Sin intercambios | Termina |

> En la primera etapa de la tercera pasada ya no se realizan intercambios, por lo que la ejecución termina.

### ✅ Ejercicios para el estudiante

1. Ordene `A = [29, 11, 42, 08, 35, 17, 24]` con Shaker Sort. Registre el último intercambio de cada etapa y los nuevos límites IZQ y DER. *(solución en Anexo B)*
2. Aplique el método a `A = [05, 07, 09, 12, 11, 15, 18]`. Explique en qué momento la ausencia de intercambios permite concluir el proceso. *(solución en Anexo B)*

### 💡 Notas y memoria/eficiencia

- Tiempo: O(n²) peor caso, pero **mejor que burbuja en la práctica** (el intervalo activo se encoge por ambos lados usando K).
- Mejor caso O(n) en datos casi ordenados. Memoria O(1) · **Estable: Sí**.
- Se clasifica como **"directo mejorado"** en la síntesis de los apuntes.

---

## 4. Ordenación por inserción directa

### 🗣️ En palabras

**Analogía:** es el **método de la baraja**: como cuando ordenas cartas en la mano, tomas una carta nueva y la **insertas en la parte izquierda que ya está ordenada**, deslizando hacia la derecha las que sean mayores.

**Descripción directa:** su idea central es insertar cada elemento `A[I]` en la parte izquierda del arreglo que ya se encuentra ordenada. El proceso se aplica desde el **segundo elemento hasta el n-ésimo**.

### 📋 Cómo se ejecuta

1. Tomar `A[I]` como elemento `AUX`.
2. Comparar `AUX` con los elementos de la parte izquierda, empezando en `K = I − 1`.
3. Mientras `AUX` sea menor que `A[K]`, desplazar `A[K]` una posición a la derecha y decrementar `K`.
4. Colocar `AUX` en `A[K + 1]`.
5. Continuar con el siguiente `I`.

### 📘 Algoritmo del libro

**Algoritmo 8.5 · Inserción**
```
Variables: I, AUX, K enteros
1. Repetir con I desde 2 hasta N
   Hacer AUX ← A[I] y K ← I − 1
   1.1 Mientras ((K >= 1) y (AUX < A[K])) repetir
       Hacer A[K+1] ← A[K] y K ← K − 1
   {fin del ciclo}
   Hacer A[K+1] ← AUX
{fin del ciclo}
```

### 🧮 Ejemplo 8.4 del libro

Arreglo inicial: `A = [15, 67, 08, 16, 44, 27, 12, 35]`.

| Pasada | Arreglo (la parte izquierda queda ordenada) |
|---|---|
| Inicial | 15 67 08 16 44 27 12 35 |
| 1.ª (inserta 67) | 15 67 08 16 44 27 12 35 |
| 2.ª (inserta 08) | 08 15 67 16 44 27 12 35 |
| 3.ª (inserta 16) | 08 15 16 67 44 27 12 35 |
| … | … hasta [08 12 15 16 27 35 44 67] |

> Una vez localizada la posición correcta del elemento, se **interrumpen las comparaciones** de esa pasada. El proceso continúa hasta obtener el arreglo ordenado.

### ✅ Ejercicios para el estudiante

1. Ordene `A = [24, 13, 18, 09, 31, 16]` mediante inserción directa. Muestre la parte izquierda ordenada después de cada pasada. *(solución en Anexo B)*
2. Ordene `A = [07, 12, 18, 25, 20, 30]`. Registre únicamente las comparaciones y desplazamientos que se producen al insertar 20. *(solución en Anexo B)*

### 💡 Notas y memoria/eficiencia

- Tiempo: O(n²) peor, pero **O(n)** si el arreglo está ordenado/casi ordenado → es el **adaptativo** por excelencia.
- Memoria O(1) · Estable: **Sí**.
- El mejor de los directos para datos que "ya casi están".
- Ver las fórmulas exactas de comparaciones y movimientos en la sección 6.

---

## 5. Ordenación por selección directa

### 🗣️ En palabras

**Analogía:** como ordenar un montón de cartas sacando **siempre la más chica** del montón y colocándola al final de la mano ordenada.

**Descripción directa:** busca el **menor elemento** del arreglo y lo coloca en la primera posición; después busca el segundo menor y lo coloca en la segunda posición. El proceso se repite sobre la parte todavía no ordenada hasta que solo queda el elemento mayor.

### 📋 Cómo se ejecuta

1. Para cada posición `I`, considerar `A[I]` como `MENOR` y guardar `K = I`.
2. Recorrer `J` desde `I + 1` hasta `N`.
3. Si `A[J] < MENOR`, actualizar `MENOR` y `K`.
4. Al terminar el recorrido, colocar en `A[I]` el valor `MENOR` e intercambiar con la posición `K`.
5. Continuar con `I + 1`.

### 📘 Algoritmo del libro

**Algoritmo 8.9 · Selección**
```
Variables: I, MENOR, K, J enteros
1. Repetir con I desde 1 hasta N − 1
   Hacer MENOR ← A[I] y K ← I
   1.1 Repetir con J desde I + 1 hasta N
       1.1.1 Si (A[J] < MENOR) entonces
                 Hacer MENOR ← A[J] y K ← J
       {fin del condicional}
   {fin del ciclo}
   Hacer A[K] ← A[I] y A[I] ← MENOR
{fin del ciclo}
```

### 🧮 Ejemplo 8.8 del libro

Arreglo inicial: `A = [15, 67, 08, 16, 44, 27, 12, 35]`.

| Estado | Arreglo |
|---|---|
| Inicial | 15 67 08 16 44 27 12 35 |
| 1.ª pasada | **08** 67 15 16 44 27 12 35 |
| 2.ª pasada | 08 **12** 15 16 44 27 67 35 |

> En la primera pasada se selecciona **08** y se intercambia con 15. En la segunda se selecciona **12** dentro de la parte no ordenada y se intercambia con 67. Las pasadas sucesivas colocan los mínimos restantes.

### ✅ Ejercicios para el estudiante

1. Ordene `A = [38, 14, 27, 09, 21, 33]` con selección directa. En cada pasada anote `MENOR` y `K` antes del intercambio. *(solución en Anexo B)*
2. Ordene `A = [04, 18, 11, 29, 07, 25]`. Muestre el arreglo después de cada una de las primeras cuatro pasadas. *(solución en Anexo B)*

### 💡 Notas y memoria/eficiencia

- **Siempre O(n²)** en comparaciones sin importar el orden inicial (no es adaptativo).
- Memoria O(1) · **Estable: No** (los intercambios a distancia pueden invertir iguales).
- **Ventaja:** hace **muy pocos movimientos** (a lo más n − 1), por eso la fuente lo considera el **mejor de los métodos directos en términos generales** (ver sección 6).

---

## 6. Análisis de eficiencia de los métodos directos

### 🗣️ En palabras

Los tres métodos directos se comparan contando cuántas **comparaciones (C)** y cuántos **movimientos (M)** hacen sobre **arreglos ordenados, desordenados y en orden inverso**. El tiempo de ejecución de todos es proporcional a **n²**, aunque el número real de movimientos difiere de forma importante.

### Resultados centrales de la fuente

- **Intercambio directo:** realiza (n² − n)/2 comparaciones; los movimientos **dependen fuertemente** de la disposición inicial.
- **Inserción directa:** puede realizar solo **n − 1 comparaciones y cero movimientos** cuando el arreglo ya está ordenado; aumentan en desordenados o inversos.
- **Selección directa:** realiza (n² − n)/2 comparaciones **independientemente** de la disposición inicial y **n − 1 movimientos** siempre.

> **Conclusión de la fuente:** *selección directa* es, en términos generales, el **mejor de los tres métodos directos**; *inserción directa* lo supera cuando el arreglo ya está ordenado; *intercambio directo* es el menos eficiente.

### Tabla de eficiencia de los métodos directos (C y M)

| Método / medida | Arreglo ordenado | Arreglo desordenado | Orden inverso |
|---|---|---|---|
| Intercambio directo · **C** | (n² − n)/2 | (n² − n)/2 | (n² − n)/2 |
| Intercambio directo · **M** | 0 | 0.75 · (n² − n) | 1.5 · (n² − n) |
| Inserción directa · **C** | **n − 1** | (n² + n − 2)/4 | (n² − n)/2 |
| Inserción directa · **M** | **0** | (n² − n)/4 | (n² − n)/2 |
| Selección directa · **C** | (n² − n)/2 | (n² − n)/2 | (n² − n)/2 |
| Selección directa · **M** | **n − 1** | **n − 1** | **n − 1** |

**Formas de leer la tabla (memorización):**

- **Intercambio:** comparaciones fijas; movimientos 0 → 0.75 → 1.5 (se triplican de ordenado a inverso... en realidad pasan de 0 a 1.5×(n²−n)).
- **Inserción:** comparaciones n−1 → ~n²/4 → n²/2; movimientos igual pero la mitad.
- **Selección:** tanto C como M son **constantes** (no les importa el orden inicial).

### ✅ Ejercicios para el estudiante

1. Para n = 20, calcule C para intercambio directo y selección directa usando C = (n² − n)/2. En selección, calcule también M = n − 1. *(solución en Anexo B)*
2. Para n = 50, compare el comportamiento de inserción directa en un arreglo ya ordenado frente a selección directa usando las fórmulas de la tabla 8.5. Indique qué método realiza menos operaciones en ese caso. *(solución en Anexo B)*

### 💡 Notas para exámenes

- Pregunta clásica: "¿por qué selección se considera mejor que intercambio?" → mismo número de comparaciones ((n²−n)/2) pero **muchísimos menos movimientos** (n−1 vs. hasta 1.5·(n²−n)).
- "¿Cuándo gana inserción?" → cuando el arreglo ya está (casi) ordenado: n−1 comparaciones y 0 movimientos.
- "¿Cuándo es peor intercambio?" → siempre que se cuenten movimientos; es el menos eficiente de los directos.

---

# ORDENACIÓN INTERNA · MÉTODOS LOGARÍTMICOS

---

## 7. Ordenación por el método de Shell

### 🗣️ En palabras

**Analogía:** es como ordenar un mazo de cartas primero "a grandes saltos": comparas cartas lejanas (cada *intervalo* de posiciones), y poco a poco acortas el salto hasta llegar a 1. Primero se arregla el caos a lo bruto y al final se afina.

**Descripción directa:** Shell es una **versión mejorada de la inserción directa**, también llamado **inserción con incrementos decrecientes**. En lugar de comparar solo elementos adyacentes, organiza grupos de elementos **separados por un intervalo. El intervalo se reduce progresivamente hasta llegar a 1.**

### 📋 Cómo se ejecuta

1. Inicializar un intervalo `INT` mayor que 1.
2. Reducir `INT` a la mitad entera.
3. Comparar elementos separados por `INT` posiciones e intercambiarlos cuando estén desordenados.
4. Repetir sobre todo el arreglo hasta que **una pasada con ese intervalo no produzca cambios**.
5. Volver a reducir `INT` y continuar hasta `INT = 1`.

### 📘 Algoritmo del libro

**Algoritmo 8.10 · Shell**
```
Variables: INT, I, AUX enteros; BAND booleana
1. Hacer INT ← N + 1
2. Mientras (INT > 1) repetir
   Hacer INT ← parte entera(INT / 2) y BAND ← VERDADERO
   2.1 Mientras (BAND = VERDADERO) repetir
       Hacer BAND ← FALSO e I ← 1
       2.1.1 Mientras ((I + INT) <= N) repetir
             Si A[I] > A[I + INT] entonces
                AUX ← A[I]; A[I] ← A[I+INT]; A[I+INT] ← AUX
                y BAND ← VERDADERO
             {fin del condicional}
             Hacer I ← I + 1
       {fin del ciclo}
   {fin del ciclo}
{fin del ciclo}
```

> Observa el uso de `BAND`: igual que en la burbuja con señal, para un mismo `INT` se repite hasta que una pasada completa no produzca ningún intercambio.

### 🧮 Ejemplo 8.9 del libro

Arreglo inicial de 16 elementos: `A = [15, 67, 08, 16, 44, 27, 12, 35, 56, 21, 13, 28, 60, 36, 07, 10]`. Los intervalos del ejemplo son **8, 4, 2 y 1**.

| Intervalo | Arreglo después de la pasada |
|---|---|
| 8 | 15 21 08 16 44 27 07 10 56 67 13 28 60 36 12 35 |
| 4 | 15 21 07 10 44 27 08 16 56 36 12 28 60 67 13 35 |
| 2 | 07 10 08 16 12 21 13 27 15 28 44 35 56 36 60 67 |
| 1 | 07 08 10 12 13 15 16 21 27 28 35 36 44 56 60 67 |

### ✅ Ejercicios para el estudiante

1. Aplique Shell a `A = [32, 14, 27, 09, 45, 18, 21, 06]` usando los intervalos que produce el algoritmo. Muestre el arreglo después de cada valor de INT. *(solución en Anexo B)*
2. Para `A = [40, 12, 35, 08, 27, 19, 31, 05, 44, 16, 23, 10, 38, 21, 29, 07]`, siga los intervalos 8, 4, 2 y 1 y registre los grupos formados en cada pasada. *(solución en Anexo B)*

### 💡 Notas y memoria/eficiencia

- Complejidad: mejor que O(n²) pero **no garantiza O(n log n)**; depende de la secuencia de intervalos.
- Memoria **O(1)** · **Estable: No** (los saltos rompen el orden de iguales).
- Gran equilibrio sencillez/velocidad; útil en sistemas con poca memoria (embebidos).
- El `INT` inicial en el libro es `N + 1`, de modo que el primer intervalo real es `parte entera((N+1)/2)` (para N=8 da 4; para N=16 da 8).

---

## 8. Ordenación por el método quicksort

### 🗣️ En palabras

**Analogía:** elige a una persona de la fila (el **pivote X**) y le pide a los más bajos que se pongan a su izquierda y a los más altos a su derecha. Con eso, esa persona ya quedó en su posición definitiva; se repite el mismo juego en cada lado.

**Descripción directa:** Quicksort (método rápido u **ordenación por partición**) toma un elemento `X` y busca **colocarlo en su posición correcta**: todo lo que queda a su izquierda es menor o igual a X, y todo lo de su derecha es mayor o igual a X. El mismo proceso se repite en los subconjuntos izquierdo y derecho.

### 📋 Cómo se ejecuta la partición

1. Seleccionar `X`; en el ejemplo del libro se elige `A[1]`.
2. Recorrer **de derecha a izquierda** mientras los elementos sean mayores o iguales a X. Al encontrar uno menor, intercambiarlo con X y mover la posición del pivote.
3. Recorrer **de izquierda a derecha** mientras los elementos sean menores o iguales a X. Al encontrar uno mayor, intercambiarlo con X.
4. **Alternar los recorridos** hasta que el pivote quede en su posición correcta.
5. Aplicar la misma partición a cada subconjunto con dos o más elementos.

### 📘 Algoritmos del libro

**Algoritmo 8.11 · Rápido_recursivo (A, N)**
```
Llamar al algoritmo Reduce_recursivo con 1 y N
```

**Algoritmo 8.12 · Reduce_recursivo (INI, FIN)**
```
Variables: IZQ, DER, POS, AUX enteros; BAND booleana
1. Hacer IZQ ← INI, DER ← FIN, POS ← INI y BAND ← VERDADERO
2. Mientras (BAND = VERDADERO) repetir
   Hacer BAND ← FALSO
   2.1 Mientras ((A[POS] <= A[DER]) y (POS ≠ DER)) repetir
       Hacer DER ← DER − 1
   2.2 Si (POS ≠ DER) entonces
       Intercambiar A[POS] y A[DER]; Hacer POS ← DER
       2.2.1 Mientras ((A[POS] >= A[IZQ]) y (POS ≠ IZQ)) repetir
             Hacer IZQ ← IZQ + 1
       2.2.2 Si (POS ≠ IZQ) entonces
             Hacer BAND ← VERDADERO
             Intercambiar A[POS] y A[IZQ]; Hacer POS ← IZQ
{fin del ciclo}
4. Si ((POS − 1) > INI) entonces
   Regresar a Reduce_recursivo con INI y (POS − 1)
5. Si (FIN > (POS + 1)) entonces
   Regresar a Reduce_recursivo con (POS + 1) y FIN
```

**Variante iterativa del libro:** sustituye las llamadas recursivas mediante **dos pilas**, `PILAMENOR` y `PILAMAYOR`, donde se almacenan los extremos izquierdo y derecho de los subconjuntos pendientes. El procedimiento de partición se conserva.

### 🧮 Ejemplo 8.11 del libro

Arreglo inicial: `A = [15, 67, 08, 16, 44, 27, 12, 35]`. Se selecciona **X = 15**.

| Paso | Acción | Arreglo |
|---|---|---|
| Inicial | X = A[1] = 15 | 15 67 08 16 44 27 12 35 |
| 1 | 12 < 15; se intercambia con el pivote | 12 67 08 16 44 27 **15** 35 |
| 2 | 67 > 15; se intercambia con el pivote | 12 **15** 08 16 44 27 67 35 |
| 3 | 08 < 15; se intercambia | 12 08 **15** 16 44 27 67 35 |
| Fin de partición | 15 queda en su posición correcta | [12, 08] \| **15** \| [16, 44, 27, 67, 35] |

El proceso continúa con cada subconjunto: primero `[12, 08]` y luego `[16, 44, 27, 67, 35]`.

### ✅ Ejercicios para el estudiante

1. Aplique una primera partición de quicksort a `A = [22, 41, 13, 35, 09, 28, 17]` tomando A[1] como pivote. Muestre cada intercambio hasta colocar el pivote. *(solución en Anexo B)*
2. Ordene `A = [34, 12, 27, 08, 19, 41, 15, 30]` siguiendo la versión recursiva. Dibuje los subconjuntos que quedan pendientes después de cada partición. *(solución en Anexo B)*

### 💡 Notas y memoria/eficiencia

- Promedio **O(n log n)**; peor caso **O(n²)** (siempre que el pivote quede muy mal repartido, p. ej. arreglo ya ordenado tomando A[1]).
- Memoria: O(log n) de pila (recursión). · **Estable: No**.
- **No es adaptativo**: no aprovecha por sí solo el orden ya existente (de hecho le molesta).
- Es el más rápido en promedio entre los estudiados.

---

## 9. Ordenación por el método heapsort (montículo)

### 🗣️ En palabras

**Analogía:** imagina una pirámide de vasos donde cada vaso es **más grande que los de abajo** (montículo máximo: el papá siempre es mayor o igual que sus hijos). Construyes la pirámide, sacas el vaso de la punta (el máximo) y lo guardas al final, recompones la pirámide y repites.

**Descripción directa:** Heapsort se basa en dos operaciones: **construir un montículo** y **eliminar repetidamente su raíz**. En el montículo máximo usado por la fuente, para todo nodo su valor debe ser **mayor o igual** que el de cualquiera de sus hijos.

### Representación del montículo en un arreglo (1-indexado)

| Relación | Posición |
|---|---|
| Nodo K | A[K] |
| Hijo izquierdo | A[2 · K] |
| Hijo derecho | A[2 · K + 1] |
| Padre del nodo K (distinto de la raíz) | A[parte entera de K/2] |

### 📋 Cómo se ejecuta

1. **Construcción:** insertar los elementos y, si un nuevo elemento es mayor que su padre, **intercambiarlo hacia arriba** hasta restablecer la propiedad del montículo.
2. **Ordenación:** intercambiar la **raíz** con el **último elemento** del montículo activo.
3. **Reacomodar** desde la raíz hacia abajo comparando con el **mayor de sus hijos**.
4. **Reducir** el tamaño activo del montículo y repetir hasta que todos los máximos hayan quedado al final del arreglo.

### 📘 Algoritmos del libro

**Algoritmo 8.13 · Inserta_montículo (A, N)**
```
Variables: I, K, AUX enteros; BAND booleana
1. Repetir con I desde 2 hasta N
   Hacer K ← I y BAND ← VERDADERO
   1.1 Mientras ((K > 1) y (BAND = VERDADERO)) repetir
       Hacer BAND ← FALSO
       1.1.1 Si (A[K] > A[parte entera(K / 2)]) entonces
                 Intercambiar A[K] con A[parte entera(K / 2)]
                 Hacer K ← parte entera(K / 2) y BAND ← VERDADERO
       {fin del condicional}
   {fin del ciclo}
{fin del ciclo}
```

**Algoritmo 8.14 · Elimina_montículo (A, N)**
```
Variables: I, AUX, IZQ, DER, K, AP, MAYOR enteros; BOOL booleana
1. Repetir con I desde N hasta 2 {descendente}
   AUX ← A[I]; A[I] ← A[1]; IZQ ← 2; DER ← 3; K ← 1; BOOL ← VERDADERO
   1.1 Mientras ((IZQ < I) y (BOOL = VERDADERO)) repetir
       Hacer MAYOR ← A[IZQ] y AP ← IZQ
       1.1.1 Si ((MAYOR < A[DER]) y (DER < I)) entonces
                 Hacer MAYOR ← A[DER] y AP ← DER
       {fin del condicional}
       1.1.3 Si (AUX < MAYOR) entonces
                 Hacer A[K] ← A[AP] y K ← AP
               si no Hacer BOOL ← FALSO
       Hacer IZQ ← K * 2 y DER ← IZQ + 1
   {fin del ciclo}
   Hacer A[K] ← AUX
{fin del ciclo}
```

**Algoritmo 8.15 · Montículo (A, N)**
```
Llamar al algoritmo Inserta_montículo con A y N
Llamar al algoritmo Elimina_montículo con A y N
```

### 🧮 Ejemplo del libro (inserción)

La fuente muestra un montículo con **raíz 67** y explica la **inserción de 63**:

1. 63 se inserta en la primera posición disponible (padre inmediato: **56**).
2. **63 sube al lugar de 56** (porque 63 > 56).
3. **63 sube al lugar de 60** (porque 63 > 60).
4. Se detiene (63 > 67 es **falso**); se conserva la propiedad del montículo.

Representación lineal después de insertar 63:
```
67, 36, 63, 28, 21, 60, 44, 27, 16, 15, 08, 35, 56
```

> En la fase de **eliminación**, cada raíz extraída se coloca al final del arreglo, de modo que los **máximos quedan ordenados de derecha a izquierda**.

### ✅ Ejercicios para el estudiante

1. Construya un montículo máximo insertando, en este orden, las claves `[18, 42, 11, 35, 27, 50, 09, 31]`. Muestre el arreglo después de cada inserción que provoque intercambio. *(solución en Anexo B)*
2. Partiendo del montículo máximo `A = [60, 44, 55, 28, 21, 35, 40, 12, 16]`, elimine la raíz dos veces y muestre el reacomodo del montículo después de cada eliminación. *(solución en Anexo B)*

### 💡 Notas y memoria/eficiencia

- Tiempo: **siempre O(n log n)** garantizado.
- Memoria: **O(1)** (in-place). · **Estable: No**.
- La construcción del montículo cuesta O(n), no O(n log n). 🧠 detalle clásico de examen.
- El valor "seguro": O(n log n) garantizado **sin memoria extra** (lo que Merge no puede prometer).

---

# ORDENACIÓN EXTERNA E INTERCALACIÓN DE ARCHIVOS

---

## 10. Ordenación externa e intercalación de archivos

### 🗣️ En palabras

Cuando los datos **no caben en memoria principal**, se organizan en **archivos** en almacenamiento secundario y se trabaja con ellos. **Intercalar** dos archivos ordenados es como barajar dos mazos ordenados: siempre tomas el registro más chico de la cara de cada archivo.

**Descripción directa:** la **intercalación** es la unión de **dos o más archivos previamente ordenados** de acuerdo con un campo clave, generando un solo archivo ordenado. Se comparan los registros actuales de F1 y F2, se escribe el menor en F3 y **solo avanza el archivo del que se tomó el registro**. Cuando uno se termina, se copian los registros restantes del otro. El proceso de combinar dos o más secuencias ordenadas en una sola se denomina **fusión o mezcla**.

### 📘 Algoritmo del libro

**Algoritmo 8.16 · Intercalación (F1, F2, F3)**
```
Variables: R1, R2 enteros; BAN1, BAN2 booleanas
1. Abrir F1 y F2 para lectura.
2. Abrir F3 para escritura.
3. Hacer BAN1 ← VERDADERO y BAN2 ← VERDADERO.
4. Mientras existan datos pendientes en F1 y F2 repetir
   Si BAN1 = VERDADERO, leer R1 de F1 y hacer BAN1 ← FALSO.
   Si BAN2 = VERDADERO, leer R2 de F2 y hacer BAN2 ← FALSO.
   Si (R1 < R2) entonces
      Escribir R1 en F3 y hacer BAN1 ← VERDADERO
   si no
      Escribir R2 en F3 y hacer BAN2 ← VERDADERO.
5. Si quedó un registro pendiente de F1, escribirlo y copiar el resto de F1.
6. Si quedó un registro pendiente de F2, escribirlo y copiar el resto de F2.
7. Cerrar F1, F2 y F3.
```

### 🧮 Ejemplo 8.19 del libro

```
F1: 06 09 18 20 35
F2: 10 16 25 28 66 82 87
```

Las primeras comparaciones son **06 < 10, 09 < 10 y 18 < 10**. Se escriben 06 y 09 desde F1; luego se escribe 10 desde F2. El proceso continúa hasta obtener el único F3 ordenado.

**Intercalación reescrita paso a paso:**

| Comparación | Registro escrito en F3 | Archivo que avanza |
|---|---|---|
| 06 frente a 10 | 06 | F1 |
| 09 frente a 10 | 09 | F1 |
| 18 frente a 10 | 10 | F2 |
| 18 frente a 16 | 16 | F2 |
| 18 frente a 25 | 18 | F1 |
| 20 frente a 25 | 20 | F1 |
| 35 frente a 25 | 25 | F2 |
| 35 frente a 28 | 28 | F2 |
| 35 frente a 66 | 35 | F1 ← F1 termina |
| Resto de F2 | 66, 82, 87 | Se copian directamente |

**F3 resultante:** `06 09 10 16 18 20 25 28 35 66 82 87`

### ✅ Ejercicios para el estudiante

1. Intercale `F1 = [03, 14, 22, 41]` y `F2 = [05, 11, 27, 30, 48]`. Muestre cada comparación y el contenido acumulado de F3. *(solución en Anexo B)*
2. Intercale `F1 = [08, 16, 19, 25, 60]` y `F2 = [04, 12, 31]`. Indique en qué momento termina uno de los archivos y cómo se copian los registros restantes. *(solución en Anexo B)*

### 💡 Notas y memoria/eficiencia

- La intercalación **presupone archivos ya ordenados**; por sí sola no ordena.
- Costo dominado por **operaciones de E/S** (lectura/escritura), no por comparaciones.
- Nota de estabilidad del libro: como la comparación es `R1 < R2`, ante un **empate** se escribe primero R2 (no conserva el orden de F1). Revisa qué política usa tu profesor para los empates.

---

## 11. Ordenación de archivos

### 🗣️ En palabras

**Descripción directa:** la **ordenación de archivos** se realiza cuando el **volumen de datos es demasiado grande para la memoria principal**. Ordenar un archivo significa **clasificar sus registros** en forma ascendente o descendente de acuerdo con un **campo clave**. La principal desventaja es el **tiempo de ejecución** originado por las sucesivas operaciones de **lectura y escritura**.

- La fuente identifica como métodos externos principales los basados en **mezcla directa** y **mezcla equilibrada**.
- La sección 8.3.2 funciona como **contextualización**: no presenta un algoritmo independiente; los procedimientos concretos son las mezclas que siguen.

### ✅ Ejercicios para el estudiante

1. Explique, con base en la definición de la fuente, por qué un conjunto de registros que **no cabe en memoria principal** requiere un método de **ordenación externa** y qué papel cumple el **campo clave**. *(solución en Anexo B)*
2. Para un archivo de registros de alumnos ordenado por una clave numérica, describa qué **operaciones de entrada/salida** hacen que la ordenación externa sea más costosa que la interna. No proponga un algoritmo distinto de los estudiados. *(solución en Anexo B)*

### 💡 Notas

- Diferencia clave vs. interna: se paga por **cada lectura/escritura de bloques en disco**, que son órdenes de magnitud más lentas que la memoria RAM.
- Lo que varía entre métodos externos es **cuántas veces se relee y reescribe el archivo completo**.

---

## 12. Ordenación por mezcla directa

### 🗣️ En palabras

**Analogía:** repartir fichas en dos platos y volver a juntarlas "de a parejas ordenadas". Empieza con bloques de 1 registro; los fusiona en bloques de 2, luego de 4, de 8… **duplicando el tamaño** en cada pasada hasta ordenar todo.

**Descripción directa:** la mezcla directa realiza sucesivamente una **partición** y una **fusión**. En la primera pasada las particiones tienen **longitud 1** y la fusión produce secuencias ordenadas de **longitud 2**; después las longitudes **se duplican**: 2 → 4 → 8 y así, hasta ordenar el archivo original. Utiliza **dos archivos auxiliares F1 y F2** (y produce de vuelta en F).

### 📋 Cómo se ejecuta

1. Inicializar `PART = 1`.
2. **Particionar** F alternadamente en F1 y F2, copiando bloques de longitud `PART`.
3. **Fusionar** bloques correspondientes de F1 y F2 hacia F, produciendo secuencias ordenadas de longitud `2 · PART`.
4. Duplicar `PART`.
5. Repetir mientras `PART < parte entera((N + 1) / 2)`.

> ⚠️ **Ojo con la condición de paro.** Tal como aparece en los apuntes, para valores de N que no son potencias de 2 la última fusión quedaría sin ejecutarse (p. ej. N = 8: con `PART < 4` se harían solo 2 pasadas y el archivo no quedaría ordenado). En la práctica (y como lo muestra el ejemplo 8.20 del libro) la regla es: **repetir mientras la longitud de secuencia sea menor que N**, es decir, ejecutar pasadas con PART = 1, 2, 4, … 8 mientras `PART < N`. Usa esta regla al resolver los ejercicios.

### 📘 Algoritmos del libro

**Algoritmo 8.17 · Mezcla_directa (F, N)**
```
Variables: PART entera
1. Hacer PART ← 1
2. Mientras (PART < N) repetir          // condición práctica; ver nota ↑
   Llamar al algoritmo Particiona con F, F1, F2 y PART
   Llamar al algoritmo Fusiona con F, F1, F2 y PART
   Hacer PART ← PART * 2
{fin del ciclo}
```

**Algoritmo 8.18 · Particiona (F, F1, F2, PART)**
```
Abrir F para lectura; abrir F1 y F2 para escritura.
Mientras no sea fin de F:
   Copiar hasta PART registros consecutivos de F hacia F1.
   Copiar hasta PART registros consecutivos de F hacia F2.
Cerrar los archivos.
```

**Algoritmo 8.19 · Fusiona (F, F1, F2, PART)**
```
Abrir F para escritura; abrir F1 y F2 para lectura.
Leer registros de F1 y F2 y fusionar, en orden, bloques de tamaño PART.
Copiar a F los registros restantes de cada bloque y, al final, los registros restantes de F1 o F2.
Cerrar los archivos.
```

### 🧮 Ejemplo 8.20 del libro

`F = [09, 75, 14, 68, 29, 17, 31, 25, 04, 05, 13, 18, 72, 46, 61]`

| Pasada | Longitud de partición | Resultado de la fusión en F |
|---|---|---|
| 1 | 1 | 09 75 \| 14 68 \| 17 29 \| 25 31 \| 04 05 \| 13 18 \| 46 72 \| 61 |
| 2 | 2 | 09 14 68 75 \| 17 25 29 31 \| 04 05 13 18 \| 46 61 72 |
| 3 | 4 | 09 14 17 25 29 31 68 75 \| 04 05 13 18 46 61 72 |
| 4 | 8 | 04 05 09 13 14 17 18 25 29 31 46 61 68 72 75 |

**Final:** `04 05 09 13 14 17 18 25 29 31 46 61 68 72 75`

### ✅ Ejercicios para el estudiante

1. Aplique mezcla directa a `F = [21, 05, 18, 09, 30, 12, 27, 03]`. Muestre F1, F2 y F después de las etapas con PART = 1, 2 y 4. *(solución en Anexo B)*
2. Aplique el método a `F = [14, 07, 25, 11, 19, 02, 31]`. Señale cómo se maneja la última partición cuando el número de registros no completa el tamaño PART. *(solución en Anexo B)*

### 💡 Notas y memoria/eficiencia

- Complejidad: O(n log n) en pasadas de lectura/escritura sobre los archivos.
- Memoria: usa **solo 2 archivos auxiliares** (F1, F2); el costo real es de **E/S en disco**.
- La longitud `PART` crece en potencias de 2 → número de pasadas = ceil(log₂ n).
- Las **particiones incompletas** (bloques < PART) se copian tal cual y se fusionan con su pareja disponible.

---

## 13. Ordenación por el método de mezcla equilibrada

### 🗣️ En palabras

**Analogía:** en lugar de partir el archivo en bloques de tamaño fijo (mezcla directa), la mezcla equilibrada **aprovecha las secuencias que ya vienen ordenadas** (ramas que no hay que volver a ordenar). Por eso también se llama **mezcla natural**.

**Descripción directa:** optimiza la mezcla directa al tomar **secuencias ya ordenadas de máxima longitud** en lugar de secuencias de tamaño fijo. Requiere el archivo original F y **tres archivos auxiliares F1, F2 y F3**. Dos actúan como entrada y dos como salida, **alternando sus funciones** durante las fusiones-particiones. Termina cuando, después de una fusión-partición, **el segundo archivo de salida queda vacío**.

### 📋 Cómo se ejecuta

1. Realizar una **partición inicial** de F identificando **secuencias ordenadas naturales** y distribuyéndolas alternadamente en **F2 y F3**.
2. **Fusionar-particcionar** F2 y F3 hacia **F y F1**.
3. **Alternar los archivos** de entrada y salida en cada nueva fusión-partición.
4. Terminar cuando, después de una fusión-partición, el **segundo archivo de salida quede vacío**.

### 📘 Algoritmos del libro

**Algoritmo 8.20 · Mezcla_equilibrada (F)**
```
Variables: BAND booleana
1. Llamar al algoritmo Partición_inicial con F, F2 y F3.
2. Llamar al algoritmo Partición_fusión con F2, F3, F y F1.
3. Hacer BAND ← FALSO.
4. Mientras ((F1 != VACÍO) o (F3 != VACÍO)) repetir
   Si (BAND = VERDADERO) entonces
      Llamar a Partición_fusión con F2, F3, F y F1
      Hacer BAND ← FALSO
   si no
      Llamar a Partición_fusión con F, F1, F2 y F3
      Hacer BAND ← VERDADERO
{fin del ciclo}
```

**Algoritmo 8.21 · Partición_inicial (F, F2, F3)**
```
Abrir F para lectura y F2/F3 para escritura.
Leer el primer registro y escribirlo en F2.
Recorrer F detectando si el registro actual mantiene o rompe el orden creciente.
Mantener una secuencia en el archivo activo mientras R >= AUX;
cuando R < AUX, alternar entre F2 y F3.
Cerrar los archivos.
```

**Algoritmo 8.22 · Partición_fusión (FA, FB, FC, FD)**
```
Abrir FA y FB para lectura; FC y FD para escritura.
Fusionar las secuencias naturales de FA y FB,
escribiendo alternadamente las nuevas secuencias en FC y FD.
Cuando una secuencia termina, continuar con la otra;
al finalizar los archivos, copiar los registros pendientes y cerrar los cuatro archivos.
```

### 🧮 Ejemplo 8.22 del libro

`F = [09, 75, 14, 68, 29, 17, 31, 25, 04, 05, 13, 18, 72, 46, 61]`

Secuencias naturales del archivo: `09 75 | 14 68 | 29 | 17 31 | 25 | 04 05 13 18 72 | 46 61`

| Etapa | Archivo | Contenido / secuencias |
|---|---|---|
| Partición inicial | F2 | 09 75 \| 29 \| 25 \| 46 61 |
| Partición inicial | F3 | 14 68 \| 17 31 \| 04 05 13 18 72 |
| 1.ª fusión-partición | F | 09 14 68 75 \| 04 05 13 18 25 46 61 72 |
| 1.ª fusión-partición | F1 | 17 29 31 |
| 2.ª fusión-partición | F2 | 09 14 17 29 31 68 75 |
| 2.ª fusión-partición | F3 | 04 05 13 18 25 46 61 72 |
| 3.ª fusión-partición | F | 04 05 09 13 14 17 18 25 29 31 46 61 68 72 75 |
| 3.ª fusión-partición | F1 | *(vacío)* → termina |

### ✅ Ejercicios para el estudiante

1. Identifique las **secuencias naturales** del archivo `F = [04, 11, 18, 03, 09, 21, 25, 07, 12, 30]` y realice la partición inicial alternando secuencias entre F2 y F3. *(solución en Anexo B)*
2. Para `F = [10, 20, 05, 15, 25, 02, 08, 18]`, ejecute la partición inicial y una primera fusión-partición. Indique cuál archivo actúa como **entrada** y cuál como **salida** en esa etapa. *(solución en Anexo B)*

### 💡 Notas y memoria/eficiencia

- Más eficiente que la mezcla directa porque **no reordena ramas ya ordenadas**: el número de pasadas depende de las secuencias naturales, no de la potencia de 2 más cercana.
- Usa **3 archivos auxiliares** (F1, F2, F3) y **alterna entrada/salida** entre pasadas.
- Criterio de término: un archivo de salida queda **vacío** → el archivo ya está totalmente ordenado.
- Es el método externo "estrella" del tema (cae seguido en parciales: detectar secuencias naturales y seguir las alternancias).

---

# SÍNTESIS FINAL

| Grupo | Método | Idea central | Dato/estructura |
|---|---|---|---|
| Directo | **Burbuja** | Intercambiar adyacentes | Arreglo |
| Directo | **Burbuja con señal** | Detener si no hay intercambios | Arreglo |
| Directo mejorado | **Sacudida** | Recorridos en ambos sentidos | Arreglo |
| Directo | **Inserción** | Insertar en parte izquierda ordenada | Arreglo |
| Directo | **Selección** | Seleccionar mínimo restante | Arreglo |
| Logarítmico / mejorado | **Shell** | Incrementos decrecientes | Arreglo |
| Logarítmico | **Quicksort** | Particionar alrededor de un pivote | Arreglo |
| Logarítmico | **Heapsort** | Montículo + eliminación de raíz | Arreglo |
| Externo | **Intercalación** | Fusionar archivos ordenados | Archivos |
| Externo | **Mezcla directa** | Partición/fusión de tamaño fijo creciente | Archivos |
| Externo | **Mezcla equilibrada** | Secuencias naturales + fusión-partición | Archivos |

**Fuentes utilizadas en los apuntes:** Capítulo 8 *Métodos de ordenación* (Oswaldo Cairo, 3.ª ed.) · Capítulo 9 *Métodos de búsqueda* (usado solo para articular el tema 2.1.2) · *Apuntes_Unidad_2_ARREGLOS.pdf*.

---

# ANEXO A · Recursos visuales

Clásicos (recomendados para estudiar):
- **visuAlgo** — paso a paso con pseudocódigo: https://visualgo.net/en/sorting
- **Data Structure Visualizations (USF)** — animaciones para casi todo: https://www.cs.usfca.edu/~galles/visualization/Algorithms.html
- **The Sound of Sorting** — animaciones con audio: https://panthema.net/2013/sound-of-sorting/

Interactivos / comparativos:
- **SortVisualizer** — barras con colores por operación: https://sortvisualizer.com/
- **SortSim** — anima más de 14 algoritmos (Shell, Comb, Gnome, TimSort…): https://sortsim.dev/
- **AllTools Sorting Visualizer** — corre varios algoritmos en "carrera" y genera el peor caso: https://alltools.dev/tools/visualizations/sorting-algorithm-visualizer/
- **EasySorting** — cargás tu propio arreglo y ves cada pasada: https://easysorting.netlify.app/

>Sugerencia: empezá en **visuAlgo** paso a paso y usá **AllTools en modo carrera** para ver cuántas operaciones menos hace un logarítmico vs. un directo sobre los mismos datos.

---

# ANEXO B · Soluciones de los ejercicios

## Sección 1 — Burbuja

**Ejercicio 1** · `A = [42, 18, 35, 07, 26, 11]`, variante menor a la izquierda.

| Pasada | Arreglo al terminar |
|---|---|
| 1.ª | 07 42 18 35 11 26 |
| 2.ª | 07 11 42 18 35 26 |
| 3.ª | 07 11 18 42 26 35 |
| 4.ª | 07 11 18 26 42 35 |
| 5.ª | 07 11 18 26 35 42 |

**Ejercicio 2** · `A = [31, 12, 48, 09, 25, 17]`, variante mayor a la derecha.

| Pasada | Elemento que queda fijo | Arreglo al terminar |
|---|---|---|
| 1.ª | 48 (derecha) | 12 31 09 25 17 **48** |
| 2.ª | 31 | 12 09 25 17 **31 48** |
| 3.ª | 25 | 09 12 17 **25 31 48** |
| 4.ª | 17 | 09 12 **17 25 31 48** |
| 5.ª | 12 | 09 **12 17 25 31 48** |

Final: `[09, 12, 17, 25, 31, 48]`.

## Sección 2 — Burbuja con señal

**Ejercicio 1** · `A = [08, 12, 15, 27, 16, 35, 44]`. En la **1.ª pasada** hay un intercambio (27 y 16). En la **2.ª pasada** ya no hay intercambios → `BAND` queda VERDADERO y el algoritmo **se detiene en la pasada 2**. El último intercambio ocurrió en la pasada 1.

**Ejercicio 2** · `A = [05, 10, 15, 20, 25]`. `BAND` inicia la pasada en **VERDADERO** y finaliza en **VERDADERO** (no hubo ningún intercambio). Como `BAND` no se puso en FALSO, el ciclo termina **después de la primera pasada**; no se requieren las n − 1 = 4 pasadas porque el arreglo ya estaba ordenado.

## Sección 3 — Sacudida

**Ejercicio 1** · `A = [29, 11, 42, 08, 35, 17, 24]`.

| Etapa | Arreglo resultante | Último intercambio (K) | Nuevo límite |
|---|---|---|---|
| Inicial | 29 11 42 08 35 17 24 | — | IZQ = 2, DER = 7 |
| P1–E1 | 08 29 11 42 17 35 24 | K = 2 | IZQ = 3 |
| P1–E2 | 08 11 29 17 35 24 42 | K = 7 | DER = 6 |
| P2–E1 | 08 11 17 29 24 35 42 | K = 4 | IZQ = 5 |
| P2–E2 | 08 11 17 24 29 35 42 | K = 5 | DER = 4 |

Ahora `DER (4) < IZQ (5)` → termina. Final: `[08, 11, 17, 24, 29, 35, 42]`.

**Ejercicio 2** · `A = [05, 07, 09, 12, 11, 15, 18]`. En la etapa descendente de la **1.ª pasada** hay un único intercambio (12 y 11, K = 5) → `IZQ = 6`. En la etapa ascendente (de IZQ=6 a DER=7) **no hay intercambios** → `K` no cambia y `DER = K − 1 = 4`. Como `DER (4) < IZQ (6)`, el proceso concluye después de esa primera pasada. La ausencia de intercambios en la etapa ascendente hace que el intervalo activo se cierre de inmediato.

## Sección 4 — Inserción directa

**Ejercicio 1** · `A = [24, 13, 18, 09, 31, 16]`. Parte izquierda ordenada después de cada pasada:

| Pasada (inserta) | Arreglo |
|---|---|
| 13 | 13 24 \| 18 09 31 16 |
| 18 | 13 18 24 \| 09 31 16 |
| 09 | 09 13 18 24 \| 31 16 |
| 31 | 09 13 18 24 31 \| 16 |
| 16 | 09 13 16 18 24 31 |

Final: `[09, 13, 16, 18, 24, 31]`.

**Ejercicio 2** · Al insertar **20** en `[07, 12, 18, 25, 20, 30]` (I = 5, key = 20, K = 4):
- Compara con 25 → 25 > 20: **1 comparación, 1 desplazamiento** (`A[5] ← A[4]`), K = 3.
- Compara con 18 → 18 < 20: **1 comparación, 0 desplazamientos** (interrumpe).
- Inserta 20 en posición 4.

Resultado: **2 comparaciones y 1 desplazamiento** → `[07, 12, 18, 20, 25, 30]`.

## Sección 5 — Selección directa

**Ejercicio 1** · `A = [38, 14, 27, 09, 21, 33]`.

| Paso | MENOR | K (antes del intercambio) | Arreglo después |
|---|---|---|---|
| I=1 | 09 | 4 | 09 14 27 38 21 33 |
| I=2 | 14 | 2 (ya en su lugar) | 09 14 27 38 21 33 |
| I=3 | 21 | 5 | 09 14 21 38 27 33 |
| I=4 | 27 | 5 | 09 14 21 27 38 33 |
| I=5 | 33 | 6 | 09 14 21 27 33 38 |

**Ejercicio 2** · `A = [04, 18, 11, 29, 07, 25]`.

| Pasada | Arreglo después |
|---|---|
| 1.ª | 04 18 11 29 07 25 (mínimo 04 ya en su lugar) |
| 2.ª | 04 **07** 11 29 18 25 |
| 3.ª | 04 07 11 29 18 25 (11 ya en su lugar) |
| 4.ª | 04 07 11 **18** 29 25 |

## Sección 6 — Análisis de eficiencia

**Ejercicio 1** · n = 20.
- C (intercambio) = C (selección) = (20² − 20)/2 = (400 − 20)/2 = **190**.
- M (selección) = n − 1 = **19**.

**Ejercicio 2** · n = 50.
- Inserción en arreglo **ya ordenado**: C = n − 1 = **49 comparaciones**, M = **0 movimientos**.
- Selección: C = (2500 − 50)/2 = **1225 comparaciones**, M = 49 movimientos.
- Conclusión: **inserción directa realiza muchas menos operaciones** (49 vs. 1225) cuando el arreglo ya está ordenado; confirma que inserción "le gana" a selección en ese caso particular.

## Sección 7 — Shell

**Ejercicio 1** · `A = [32, 14, 27, 09, 45, 18, 21, 06]` (INT: 4, 2, 1).

| INT | Arreglo después del(los) pase(s) con ese intervalo |
|---|---|
| 4 | 32 14 21 06 45 18 27 09 |
| 2 | 21 06 27 09 32 14 45 18 |
| 1 | 06 09 14 18 21 27 32 45 |

**Ejercicio 2** · `A = [40, 12, 35, 08, 27, 19, 31, 05, 44, 16, 23, 10, 38, 21, 29, 07]`, intervalos 8, 4, 2, 1.

Grupos formados y estado resultante en cada pasada:

- **INT = 8** (grupos según índice mod 8): {40,44}, {12,16}, {35,23}, {08,10}, {27,38}, {19,21}, {31,29}, {05,07}
  → `40 12 23 08 27 19 29 05 44 16 35 10 38 21 31 07`
- **INT = 4** (residuo mod 4): {40,27,44,38}, {12,19,16,21}, {23,29,35,31}, {08,05,10,07}
  → `27 12 23 05 38 16 29 07 40 19 31 08 44 21 35 10`
- **INT = 2** (paridad de posición): impares {27,23,38,29,40,31,44,35}, pares {12,05,16,07,19,08,21,10}
  → `23 05 27 07 29 08 31 10 35 12 38 16 40 19 44 21`
- **INT = 1** (inserción normal)
  → `05 07 08 10 12 16 19 21 23 27 29 31 35 38 40 44`

## Sección 8 — Quicksort

**Ejercicio 1** · `A = [22, 41, 13, 35, 09, 28, 17]`, pivote X = A[1] = 22.

| Paso | Acción | Arreglo |
|---|---|---|
| Inicial | X = 22 | 22 41 13 35 09 28 17 |
| 1 | 17 < 22 → intercambia con el pivote | 17 41 13 35 09 28 **22** |
| 2 | 41 > 22 → intercambia con el pivote | 17 **22** 13 35 09 28 41 |
| 3 | 09 < 22 → intercambia | 17 09 13 35 **22** 28 41 |
| 4 | 35 > 22 → intercambia | 17 09 13 **22** 35 28 41 |
| Fin de partición | 22 en su posición | [17, 09, 13] \| **22** \| [35, 28, 41] |

**Ejercicio 2** · `A = [34, 12, 27, 08, 19, 41, 15, 30]` (recursivo). Subconjuntos pendientes tras cada partición:

- Partición 1 (X=34): `[30,12,27,08,19,15] | 34 | [41]`
- Partición de `[30,12,27,08,19,15]` (X=30): `[15,12,27,08,19] | 30` (41 ya en su lugar)
- Partición de `[15,12,27,08,19]` (X=15): `[08,12] | 15 | [27,19]`
- `[08,12]` (X=08) → `08 | [12]`. `[27,19]` (X=27) → `[19] | 27`

Final: `[08, 12, 15, 19, 27, 30, 34, 41]`.

## Sección 9 — Heapsort

**Ejercicio 1** · Insertar `[18, 42, 11, 35, 27, 50, 09, 31]` en un montículo máximo. Arreglo después de cada inserción que provoca intercambio:

| Inserción | Intercambio(s) | Montículo |
|---|---|---|
| 18 | — | 18 |
| 42 | 42 sube sobre 18 | 42 18 |
| 11 | — | 42 18 11 |
| 35 | 35 sube sobre 18 | 42 35 11 18 |
| 27 | — | 42 35 11 18 27 |
| 50 | 50 sobre 11, luego sobre 42 | 50 35 42 18 27 11 |
| 09 | — | 50 35 42 18 27 11 09 |
| 31 | 31 sube sobre 18 | 50 35 42 31 27 11 09 18 |

Montículo máximo final: `[50, 35, 42, 31, 27, 11, 09, 18]`.

**Ejercicio 2** · Montículo `[60, 44, 55, 28, 21, 35, 40, 12, 16]`, eliminar la raíz dos veces.

- **1.ª eliminación:** intercambia raíz (60) con el último (16) → se reacomoda hundiendo el 16 comparándolo con el mayor de sus hijos (55, luego 40). Reacomodo: **`[55, 44, 40, 28, 21, 35, 16, 12]`** (60 ya en su lugar).
- **2.ª eliminación:** intercambia raíz (55) con el último activo (12) → se reacomoda hundiendo el 12 (44, luego 28). Reacomodo: **`[44, 28, 40, 12, 21, 35, 16]`** (55 y 60 ya colocados).

## Sección 10 — Intercalación

**Ejercicio 1** · `F1 = [03, 14, 22, 41]`, `F2 = [05, 11, 27, 30, 48]`.

| Comparación | Escrito en F3 | F3 acumulado |
|---|---|---|
| 03 vs 05 | 03 | 03 |
| 14 vs 05 | 05 | 03 05 |
| 14 vs 11 | 11 | 03 05 11 |
| 14 vs 27 | 14 | 03 05 11 14 |
| 22 vs 27 | 22 | 03 05 11 14 22 |
| 41 vs 27 | 27 | 03 05 11 14 22 27 |
| 41 vs 30 | 30 | 03 05 11 14 22 27 30 |
| 41 vs 48 | 41 (termina F1) | 03 05 11 14 22 27 30 41 |
| resto de F2 | 48 | 03 05 11 14 22 27 30 41 48 |

**Ejercicio 2** · `F1 = [08, 16, 19, 25, 60]`, `F2 = [04, 12, 31]`.

- Escriben 04 (F2), 08 (F1), 12 (F2), 16 (F1), 19 (F1), 25 (F1), 31 (F2).
- **F2 se termina al escribir su último registro (31).** A partir de ahí **se copia directamente el resto de F1**, que es el 60.
- F3 final: `[04, 08, 12, 16, 19, 25, 31, 60]`.

## Sección 11 — Ordenación de archivos

**Ejercicio 1.** Un conjunto de registros que no cabe en memoria principal **no puede ser ordenado por los métodos internos**, porque estos asumen que el arreglo completo está disponible en RAM. La **ordenación externa** trabaja con los datos **en archivos de almacenamiento secundario**, ordenando el archivo de acuerdo con un **campo clave**: es el campo por el que se comparan los registros para decidir el orden ascendente o descendente.

**Ejercicio 2.** Las operaciones de E/S que encarecen la ordenación externa son las **múltiples lecturas y escrituras de bloques/registros en disco**: abrir/cerrar archivos, particionar el archivo original hacia archivos auxiliares y volver a leerlos y reescribirlos en cada fusión. El acceso a almacenamiento secundario es **órdenes de magnitud más lento** que la memoria principal, y las mezclas requieren releer y reescribir el archivo completo en cada pasada.

## Sección 12 — Mezcla directa

**Ejercicio 1** · `F = [21, 05, 18, 09, 30, 12, 27, 03]`.

| PART | F1 | F2 | F (tras reunir) |
|---|---|---|---|
| 1 | 21 18 30 27 | 05 09 12 03 | 05 21 09 18 12 30 03 27 |
| 2 | 05 21 12 30 | 09 18 03 27 | 05 09 18 21 03 12 27 30 |
| 4 | 05 09 18 21 | 03 12 27 30 | **03 05 09 12 18 21 27 30** |

**Ejercicio 2** · `F = [14, 07, 25, 11, 19, 02, 31]` (N = 7).

| PART | F1 | F2 | F |
|---|---|---|---|
| 1 | 14 25 19 31 | 07 11 02 | 07 14 11 25 02 19 31 |
| 2 | 07 14 02 19 | 11 25 31 | 07 11 14 25 02 19 31 |
| 4 | 07 11 14 25 | 02 19 31 | **02 07 11 14 19 25 31** |

**Manejo de la partición incompleta:** cuando un archivo no completa el tamaño PART (p. ej. F2 con `11 25 31` en PART=2, o el bloque final `31` en PART=1), el **bloque incompleto se copia tal cual** a su archivo y, al fusionar, su pareja puede tener menos elementos: de todos modos se mezclan en orden y el resto se anexa al resultado (así `[02,19]` + `[31]` → `[02,19,31]`).

## Sección 13 — Mezcla equilibrada

**Ejercicio 1** · `F = [04, 11, 18, 03, 09, 21, 25, 07, 12, 30]`.

Secuencias naturales: **`04 11 18`** · `03 09 21 25` · `07 12 30`

Partición inicial (alternando): **F2 = `04 11 18 | 07 12 30`** · F3 = `03 09 21 25`

**Ejercicio 2** · `F = [10, 20, 05, 15, 25, 02, 08, 18]`.

- Secuencias naturales: `10 20` · `05 15 25` · `02 08 18`.
- Partición inicial: **F2 = `10 20 | 02 08 18`**, **F3 = `05 15 25`**.
- 1.ª fusión-partición → **entradas: F2 y F3**; **salidas: F y F1**:
  - F = `05 10 15 20 25` (fusión de las dos primeras secuencias)
  - F1 = `02 08 18` (secuencia sin pareja)

---

# ANEXO C · Regla de oro para exámenes

**Estables (conservan el orden de claves iguales):** burbuja (intercambio directo), burbuja con señal, sacudida, inserción directa y las mezclas de tipo merge. → Nemotecnia: los que **intercambian/desplazan adyacentes** o **fusionan**.

**No estables:** selección directa, Shell, Quicksort, Heapsort.

**Adaptativos (mejoran si los datos están casi ordenados):** inserción directa (el campeón), burbuja con señal, sacudida. **No adaptativos:** selección (siempre O(n²)).

**Memoria mínima O(1) (in-place):** burbuja, su señal, sacudida, inserción, selección, Shell y Heapsort. **Memoria extra:** Quicksort (O(log n) de pila) y Merge/mezclas (archivos auxiliares o arreglos temporales).

**Tiempo garantizado O(n log n):** Merge y Heapsort. **Promedio O(n log n) con riesgo O(n²) en peor caso:** Quicksort (pivote malo).

**Preguntas trampa típicas:**

1. ¿Cuál directo es "el mejor en términos generales"? → **Selección directa** (mismos C, pero solo n−1 movimientos).
2. ¿Cuándo le gana inserción a selección? → Cuando el arreglo **ya está (casi) ordenado** (n−1 comparaciones, 0 movimientos).
3. ¿Cuál método directo es el menos eficiente? → **Intercambio directo (burbuja)** por sus movimientos.
4. ¿Cuál se detiene anticipadamente si no hubo intercambios? → **Burbuja con señal** (y la sacudida lo aprovecha en sus etapas).
5. ¿Cuál divide "particionando" alrededor de un pivote y ordena a la vez? → **Quicksort**.
6. ¿Cuál construye una pirámide y va sacando el máximo? → **Heapsort**; en la representación 1-indexada, hijo izq = 2K, hijo der = 2K+1, padre = entero(K/2).
7. Métodos externos: ¿cuál usa tamaño fijo creciente (1, 2, 4, 8…) y cuál usa secuencias naturales? → **Mezcla directa** (fijo) vs. **mezcla equilibrada** (natural).
8. ¿Cómo termina la mezcla equilibrada? → Cuando un **archivo de salida queda vacío**.
9. ¿Intercalación para qué presupone los archivos? → Que **ya están ordenados**.

**Criterio de decisión en un problema (resumen):**

| Situación | Método sugerido |
|---|---|
| Datos casi ordenados, arreglo pequeño | Inserción directa |
| Garantizar O(n log n) con memoria mínima | Heapsort |
| Garantizar O(n log n) y estabilidad | Merge (mezclas) |
| Velocidad promedio máxima | Quicksort |
| Pocos movimientos / "escrituras caras" | Selección directa |
| Datos que no caben en RAM | Mezcla equilibrada (externa) |
| Aprender "por dónde empezar" | Burbuja → señal → sacudida → inserción → selección |