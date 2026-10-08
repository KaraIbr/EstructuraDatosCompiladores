"""Ordenamiento por selección directa.

Busca el menor en el intervalo no ordenado y lo coloca en su
posición final, avanzando de izquierda a derecha.
"""

PSEUDO = [
    "Repetir con I desde 1 hasta N-1 (posición donde va el siguiente menor).",
    "Suponer que el menor del intervalo es A[I], plantear K = I.",
    "Recorrer J desde I+1 hasta N: si A[J] < MENOR, actualizar MENOR y K = J.",
    "Si K != I, intercambiar A[I] con A[K] (el MENOR queda fijo en A[I]).",
    "Avanzar a la siguiente posición; cada posición queda fija con su menor.",
]

NOTAS = {
    "peor": "O(n^2)",
    "mejor": "O(n^2)",
    "promedio": "O(n^2)",
    "memoria": "O(1)",
    "estable": "No (puede saltarse el orden de elementos iguales)",
    "adaptativo": "No (siempre recorre el intervalo completo)",
}


def ordenar(datos):
    """Devuelve una copia ordenada de datos sin modificar el original."""
    arr = list(datos)
    n = len(arr)
    for i in range(n - 1):
        k = i
        for j in range(i + 1, n):
            if arr[j] < arr[k]:
                k = j
        if k != i:
            arr[i], arr[k] = arr[k], arr[i]
    return arr


def pasos(datos):
    """Generador para animación: emite (lista, evento, i, j) en cada paso."""
    arr = list(datos)
    n = len(arr)
    yield list(arr), "inicio", None, None
    for i in range(n - 1):
        k = i
        yield list(arr), "pasada", i, None
        for j in range(i + 1, n):
            yield list(arr), "comparar", j, k
            if arr[j] < arr[k]:
                k = j
                yield list(arr), "marcar", j, None
        if k != i:
            arr[i], arr[k] = arr[k], arr[i]
            yield list(arr), "intercambiar", i, k
    yield list(arr), "fin", None, None