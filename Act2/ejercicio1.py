"""Ejercicio 1: menu interactivo de gestion de vector.

Ejercicio base de la practica "Manipulacion de Vectores".
Mantiene un vector en memoria y expone cinco operaciones basicas
dentro de un bucle `while True` hasta que la persona elige salir.

Todos los datos (tamano N, elementos, rango aleatorio y valor a
buscar) se leen por consola con input(): no hay nada hardcodeado.
"""

import random


def llenar_manual(vector):
    """Pide N y luego N valores por consola; devuelve el vector lleno.

    Complejidad temporal: O(N), una lectura por posicion.
    Complejidad espacial: O(N), solo el propio vector solicitado.
    """
    n = int(input("  tamano N del vector: "))
    while n < 0:
        print("  N no puede ser negativo.")
        n = int(input("  tamano N del vector: "))
    vector.clear()
    for i in range(n):
        vector.append(int(input(f"  elemento [{i}]: ")))
    return vector


def llenar_aleatorio(vector):
    """Llena el vector con valores aleatorios en un rango dado por consola.

    Complejidad temporal: O(N), una generacion por posicion.
    Complejidad espacial: O(N), solo el propio vector solicitado.
    """
    n = int(input("  tamano N del vector: "))
    while n < 0:
        print("  N no puede ser negativo.")
        n = int(input("  tamano N del vector: "))
    limite_inferior = int(input("  rango inferior: "))
    limite_superior = int(input("  rango superior: "))
    while limite_superior < limite_inferior:
        print("  el superior debe ser mayor o igual al inferior.")
        limite_superior = int(input("  rango superior: "))
    vector.clear()
    for _ in range(n):
        vector.append(random.randint(limite_inferior, limite_superior))
    return vector


def mostrar(vector):
    """Imprime cada elemento en formato [indice]:valor.

    Complejidad temporal: O(N), un acceso por posicion.
    Complejidad espacial: O(1), no crea estructuras nuevas.
    """
    if not vector:
        print("  el vector esta vacio.")
        return
    for i, valor in enumerate(vector):
        print(f"  [{i}]:{valor}")


def buscar_secuencial(vector, objetivo):
    """Busqueda secuencial que reporta TODOS los indices de aparicion.

    Complejidad temporal: O(N), un unico recorrido lineal.
    Complejidad espacial: O(1), solo la lista de indices coincidentes
    (crece como numero de apariciones, no como N).
    """
    indices = []
    for i, valor in enumerate(vector):
        if valor == objetivo:
            indices.append(i)
    return indices


def main():
    """Bucle del menu con las cinco opciones del ejercicio."""
    print("ejercicio 1: menu interactivo de gestion de vector")
    vector = []

    while True:
        print("\n--- MENU ---")
        print("  1. Llenar vector manualmente")
        print("  2. Llenar vector aleatoriamente")
        print("  3. Mostrar elementos actuales")
        print("  4. Buscar elemento")
        print("  5. Salir")
        opcion = input("opcion: ").strip()

        if opcion == "1":
            llenar_manual(vector)
            print("  vector llenado.")
        elif opcion == "2":
            llenar_aleatorio(vector)
            print("  vector llenado con valores aleatorios.")
        elif opcion == "3":
            print("  contenido:")
            mostrar(vector)
        elif opcion == "4":
            objetivo = int(input("  valor a buscar: "))
            indices = buscar_secuencial(vector, objetivo)
            if indices:
                print(f"  {objetivo} aparece en {len(indices)} ocurrencia(s):")
                for i in indices:
                    print(f"    indice [{i}]")
            else:
                print(f"  {objetivo} no se encuentra en el vector.")
        elif opcion == "5":
            print("hasta luego.")
            break
        else:
            print("  opcion invalida, intente de nuevo.")


if __name__ == "__main__":
    main()
