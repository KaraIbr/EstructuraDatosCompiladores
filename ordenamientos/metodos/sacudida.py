"""Ordenamiento por sacudida (Shaker Sort / sacudida bidireccional).

Mejora de la burbuja con señal: alterna el recorrido de derecha a
izquierda y de izquierda a derecha, acortando el intervalo activo
con cada pasada. Adaptativo: si una etapa no intercambia nada,
el intervalo se cierra y termina antes.
"""

PSEUDO = [
    "Definir los límites del intervalo activo: IZQ = 1 y DER = N.",
    "Mientras DER >= IZQ:",
    "    1. Etapa 1: recorrer de DER hacia IZQ comparando vecinos e intercambiando; guardar la posición K del último cambio.",
    "       Hacer IZQ = K + 1.",
    "    2. Etapa 2: recorrer de IZQ hacia DER comparando e intercambiando; guardar la posición K del último cambio.",
    "       Hacer DER = K - 1.",
    "Si alguna etapa no intercambia nada, el intervalo se colapsa y se termina.",
]

NOTAS = {
    "peor": "O(n^2)",
    "mejor": "O(n)",
    "promedio": "O(n^2)",
    "memoria": "O(1)",
    "estable": "Sí",
    "adaptativo": "Sí (se cierra pronto si no hay cambios)",
}


def ordenar(datos):
    """Devuelve una copia ordenada de datos sin modificar el original."""
    arr = list(datos)
    n = len(arr)
    izq = 0
    der = n - 1
    while der >= izq:
        k = der
        for j in range(der, izq, -1):
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
                k = j - 1
        izq = k + 1
        k = izq
        for j in range(izq, der):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                k = j
        der = k - 1
    return arr


def pasos(datos):
    """Generador para animación: emite (lista, evento, i, j) en cada paso."""
    arr = list(datos)
    n = len(arr)
    yield list(arr), "inicio", None, None
    pasada = 1
    izq = 0
    der = n - 1
    while der >= izq:
        yield list(arr), "pasada", pasada, "izq->der"
        k = der
        for j in range(der, izq, -1):
            yield list(arr), "comparar", j - 1, j
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
                k = j - 1
                yield list(arr), "intercambiar", j - 1, j
        izq = k + 1
        yield list(arr), "pasada", pasada + 0.5, "der->izq"
        k = izq
        for j in range(izq, der):
            yield list(arr), "comparar", j, j + 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                k = j
                yield list(arr), "intercambiar", j, j + 1
        der = k - 1
        pasada += 1
    yield list(arr), "fin", None, None