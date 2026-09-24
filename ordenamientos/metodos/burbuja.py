"""Módulo del ordenamiento por burbuja (intercambio directo).

Variante clásica del libro de Cairo (cap. 8): el elemento menor
"burbujea" hacia la izquierda en cada pasada.
"""

PSEUDO = [
    "Repetir con I desde 1 hasta N-1 (una pasada por elemento).",
    "Recorrer J desde N hacia abajo hasta I+1.",
    "Comparar los vecinos A[J-1] y A[J].",
    "Si A[J-1] > A[J], intercambiarlos (el menor sube a la izquierda).",
    "Al terminar la pasada, el menor quedó fijo en A[I].",
]

NOTAS = {
    "peor": "O(n^2)",
    "mejor": "O(n^2)",
    "promedio": "O(n^2)",
    "memoria": "O(1)",
    "estable": "Sí",
    "adaptativo": "No (siempre hace todas las comparaciones)",
}


def ordenar(datos):
    """Devuelve una copia ordenada de datos sin modificar el original."""
    arr = list(datos)
    n = len(arr)
    for i in range(1, n):
        for j in range(n - 1, i - 1, -1):
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
    return arr


def pasos(datos):
    """Generador para animación: emite (lista, evento, i, j) en cada paso."""
    arr = list(datos)
    n = len(arr)
    yield list(arr), "inicio", None, None
    for i in range(1, n):
        yield list(arr), "pasada", i, None
        for j in range(n - 1, i - 1, -1):
            yield list(arr), "comparar", j - 1, j
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
                yield list(arr), "intercambiar", j - 1, j
    yield list(arr), "fin", None, None