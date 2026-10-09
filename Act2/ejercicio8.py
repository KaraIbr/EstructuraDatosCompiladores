"""Ejercicio 8: reordenamiento por paridad (particion in-place).

Reorganiza el vector de modo que todos los numeros pares queden a la
izquierda y todos los impares a la derecha, usando la tecnica de DOS
PUNTEROS CRUZADOS (izq y der) sin crear arreglos auxiliares, listas
temporales ni usar sorted() (memoria O(1)).

Algoritmo:
    izq avanza desde la izquierda mientras encuentre pares;
    der avanza desde la derecha mientras encuentre impares;
    cuando ambos apuntan a elementos mal ubicados se intercambian;
    el proceso termina cuando los punteros se cruzan.
"""


def particion_paridad(vector):
    """Reordena in-place pares a la izquierda e impares a la derecha.

    Complejidad temporal: O(N), cada puntero recorre el vector una
    sola vez y los intercambios son O(1).
    Complejidad espacial: O(1), unicamente dos indices y un temporal.
    """
    izq = 0
    der = len(vector) - 1

    while izq < der:
        # izq avanza mientras el elemento ya este bien (par)
        while izq < der and vector[izq] % 2 == 0:
            izq += 1
        # der avanza mientras el elemento ya este bien (impar)
        while izq < der and vector[der] % 2 != 0:
            der -= 1
        # ambos apuntan a elementos fuera de lugar: se cruzan
        if izq < der:
            vector[izq], vector[der] = vector[der], vector[izq]
            izq += 1
            der -= 1
    return vector


def leer_vector():
    """Lee N y N elementos por consola.

    Complejidad temporal: O(N). Complejidad espacial: O(N), la
    entrada que pide el enunciado.
    """
    n = int(input("tamano N del vector: "))
    while n <= 0:
        print("N debe ser mayor que cero.")
        n = int(input("tamano N del vector: "))
    vector = []
    for i in range(n):
        vector.append(int(input(f"elemento [{i}]: ")))
    return vector


def main():
    """Flujo completo: lectura, particion de dos punteros y reporte."""
    print("ejercicio 8: reordenamiento por paridad (dos punteros cruzados)")
    vector = leer_vector()
    print(f"antes   : {vector}")

    particion_paridad(vector)
    print(f"despues: {vector}")

    # verificacion simple de la particion pedida
    region_pares = True
    seccion_impares = False
    for valor in vector:
        if valor % 2 != 0:
            seccion_impares = True
        elif seccion_impares:
            region_pares = False
    print("cumple pares a la izquierda / impares a la derecha:",
          "si" if region_pares else "no")


if __name__ == "__main__":
    main()
