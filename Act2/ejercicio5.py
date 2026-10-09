"""Ejercicio 5: fusion eficiente de dos vectores ordenados (merge).

Recibe dos vectores A (tamano N) y B (tamano M) ordenados de forma
ascendente y los fusiona en un vector C de tamano N+M usando la
tecnica de DOS PUNTEROS en un solo recorrido lineal O(N+M).

Queda prohibido concatenar y ordenar posteriormente: la fusion se
resuelve comparando los elementos apuntados por `i` y `j` y
avanzando solo el puntero que aporto el valor.
"""


def fusionar(a, b):
    """Fusiona dos vectores ordenados ascendentemente en uno nuevo.

    Complejidad temporal: O(N + M), cada puntero avanza como mucho
    N respectivamente M posiciones en una sola pasada.
    Complejidad espacial: O(N + M), solo el vector resultado C que
    pide el enunciado; no hay estructuras intermedias.
    """
    c = []
    i = 0  # puntero sobre a
    j = 0  # puntero sobre b

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1

    # queda un tramo sin consumir en uno de los dos vectores
    while i < len(a):
        c.append(a[i])
        i += 1
    while j < len(b):
        c.append(b[j])
        j += 1
    return c


def esta_ordenado(vector):
    """Verifica que el vector leido este en orden ascendente no estricto.

    Complejidad temporal: O(N), un recorrido lineal de pares.
    Complejidad espacial: O(1), solo una variable booleana.
    """
    for k in range(len(vector) - 1):
        if vector[k] > vector[k + 1]:
            return False
    return True


def leer_vector(etiqueta):
    """Lee un vector ordenado por consola y valida que este ordenado.

    Complejidad temporal: O(N). Complejidad espacial: O(N), la
    entrada que pide el enunciado.
    """
    n = int(input(f"tamano de {etiqueta}: "))
    while n < 0:
        print("el tamano no puede ser negativo.")
        n = int(input(f"tamano de {etiqueta}: "))
    vector = []
    for i in range(n):
        vector.append(int(input(f"  {etiqueta}[{i}]: ")))
    if not esta_ordenado(vector):
        print(f"aviso: {etiqueta} no estaba ordenado; el merge asciende solo "
              "si ambas entradas estan ordenadas.")
    return vector


def main():
    """Flujo completo: lectura de A y B, fusion lineal y reporte."""
    print("ejercicio 5: fusion de dos vectores ordenados (dos punteros)")
    a = leer_vector("A")
    b = leer_vector("B")

    c = fusionar(a, b)
    print(f"A ({len(a)}) = {a}")
    print(f"B ({len(b)}) = {b}")
    print(f"C ({len(c)}) = {c}   <- fusion en una sola pasada")


if __name__ == "__main__":
    main()
