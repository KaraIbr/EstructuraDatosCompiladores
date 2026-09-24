"""Ordenamiento por burbuja con señal (bandera) de intercambios.

Versión adaptativa: si en una pasada completa no hubo ningún
intercambio, el arreglo ya está ordenado y termina antes.
"""

PSEUDO = [
    "Repetir pasadas de comparación mientras se detecten cambios.",
    "Al comenzar cada pasada suponer que no habrá intercambios (BAND = Falso).",
    "Recorrer todo el arreglo comparando vecinos A[J] y A[J+1].",
    "Si están desordenados, intercambiarlos y activar BAND = Verdadero.",
    "Si al terminar la pasada BAND es Falso, el arreglo ya está ordenado: terminar.",
]

NOTAS = {
    "peor": "O(n^2)",
    "mejor": "O(n)",
    "promedio": "O(n^2)",
    "memoria": "O(1)",
    "estable": "Sí",
    "adaptativo": "Sí (termina temprano si una pasada no intercambia)",
}


def ordenar(datos):
    """Devuelve una copia ordenada de datos sin modificar el original."""
    arr = list(datos)
    n = len(arr)
    cambio = True
    while cambio:
        cambio = False
        for j in range(n - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                cambio = True
    return arr


def pasos(datos):
    """Generador para animación: emite (lista, evento, i, j) en cada paso."""
    arr = list(datos)
    n = len(arr)
    yield list(arr), "inicio", None, None
    pasada = 1
    cambio = True
    while cambio:
        cambio = False
        yield list(arr), "pasada", pasada, None
        for j in range(n - 1):
            yield list(arr), "comparar", j, j + 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                cambio = True
                yield list(arr), "intercambiar", j, j + 1
        pasada += 1
    yield list(arr), "fin", None, None