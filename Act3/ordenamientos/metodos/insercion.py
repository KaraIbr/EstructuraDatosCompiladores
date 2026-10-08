"""Ordenamiento por inserción directa (método de la baraja).

Cada elemento se inserta en su lugar dentro de la parte izquierda
que ya quedó ordenada, desplazando los mayores hacia la derecha.
"""

PSEUDO = [
    "Repetir con I desde 2 hasta N (elemento a insertar: AUX = A[I]).",
    "Iniciar K = I - 1, apuntando al último de la parte ya ordenada.",
    "Mientras K >= 1 y AUX < A[K]: desplazar A[K] hacia A[K+1] y hacer K = K - 1.",
    "Colocar AUX en A[K+1], que es el hueco que quedó.",
    "La parte izquierda del arreglo siempre permanece ordenada.",
]

NOTAS = {
    "peor": "O(n^2)",
    "mejor": "O(n)",
    "promedio": "O(n^2)",
    "memoria": "O(1)",
    "estable": "Sí",
    "adaptativo": "Sí (no desplaza si ya está en su lugar)",
}


def ordenar(datos):
    """Devuelve una copia ordenada de datos sin modificar el original."""
    arr = list(datos)
    n = len(arr)
    for i in range(1, n):
        aux = arr[i]
        k = i - 1
        while k >= 0 and aux < arr[k]:
            arr[k + 1] = arr[k]
            k -= 1
        arr[k + 1] = aux
    return arr


def pasos(datos):
    """Generador para animación: emite (lista, evento, i, j) en cada paso."""
    arr = list(datos)
    n = len(arr)
    yield list(arr), "inicio", None, None
    for i in range(1, n):
        aux = arr[i]
        k = i - 1
        yield list(arr), "pasada", i, None
        while True:
            cond = k >= 0 and aux < arr[k]
            yield list(arr), "comparar", k, i
            if not cond:
                break
            arr[k + 1] = arr[k]
            yield list(arr), "desplazar", k, k + 1
            k -= 1
        arr[k + 1] = aux
        if k + 1 != i:
            yield list(arr), "intercambiar", k + 1, i
    yield list(arr), "fin", None, None