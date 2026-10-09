"""Ejercicio 2: rotacion circular de elementos in-place.

Rota k posiciones a la derecha o a la izquierda modificando el
vector original, sin usar ningun arreglo auxiliar de tamano N
(memoria auxiliar O(1)).

Algoritmo: inversion parcial de subarreglos (reverse algorithm)
    derecha k:  invertir(0, N-1); invertir(0, k-1);  invertir(k, N-1)
    izquierda k: invertir(0, k-1); invertir(k, N-1); invertir(0, N-1)

Optimizacion previa: k = k % N (rotar N posiciones es identico a
no rotar, asi se descartan vueltas completas).
"""

import random


def invertir(vector, inicio, fin):
    """Invierte in-place el tramo vector[inicio..fin] con dos punteros.

    Complejidad temporal: O(fin - inicio + 1), lineal en el tramo.
    Complejidad espacial: O(1), solo tres variables auxiliares.
    """
    while inicio < fin:
        vector[inicio], vector[fin] = vector[fin], vector[inicio]
        inicio += 1
        fin -= 1


def rotar(vector, k, direccion):
    """Rota k posiciones in-place en la direccion indicada.

    Complejidad temporal: O(N) -> tres inversiones que recorren el
    vector completo en total.
    Complejidad espacial: O(1) -> no se crea ningun arreglo nuevo.
    """
    n = len(vector)
    if n == 0:
        return
    k = k % n  # descarta vueltas completas
    if k == 0:
        return
    if direccion == "derecha":
        invertir(vector, 0, n - 1)
        invertir(vector, 0, k - 1)
        invertir(vector, k, n - 1)
    else:  # izquierda
        invertir(vector, 0, k - 1)
        invertir(vector, k, n - 1)
        invertir(vector, 0, n - 1)


def leer_vector():
    """Lee N y N elementos por consola.

    Complejidad temporal: O(N). Complejidad espacial: O(N) (la
    entrada que pide el enunciado).
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
    """Flujo completo: lectura, rotacion y verificacion del resultado."""
    print("ejercicio 2: rotacion circular in-place (inversion parcial)")
    vector = leer_vector()
    k = int(input("posiciones k a rotar: "))
    print("direccion (derecha / izquierda):", end=" ")
    direccion = input().strip().lower()
    while direccion not in ("derecha", "izquierda"):
        print("escriba 'derecha' o 'izquierda'.")
        direccion = input("direccion: ").strip().lower()

    print(f"antes : {vector}")
    rotar(vector, k, direccion)
    print(f"despues ({direccion} x {k}): {vector}")


if __name__ == "__main__":
    main()
