"""Ordenamiento por sacudida (Shaker Sort / sacudida bidireccional).

Mejora de la burbuja con señal: alterna el recorrido de izquierda a
derecha y de derecha a izquierda, acortando el intervalo activo con
cada pasada usando la posición del último intercambio. Adaptativo:
si una etapa no intercambia nada, termina antes.
"""

PSEUDO = [
    "Definir los límites del intervalo activo: IZQ = 1 y DER = N.",
    "Mientras haya intercambios:",
    "    1. Etapa 1 (IZQ -> DER): comparar vecinos e intercambiar; guardar K del último intercambio y hacer DER = K.",
    "       Si no hubo ningún intercambio, terminar.",
    "    2. Etapa 2 (DER -> IZQ): comparar vecinos e intercambiar; guardar K del último intercambio y hacer IZQ = K.",
    "Si alguna etapa no intercambia nada, el arreglo ya está ordenado.",
]

NOTAS = {
    "peor": "O(n^2)",
    "mejor": "O(n)",
    "promedio": "O(n^2)",
    "memoria": "O(1)",
    "estable": "Sí",
    "adaptativo": "Sí (termina temprano si una etapa no intercambia)",
}


def ordenar(datos):
    """Devuelve una copia ordenada de datos sin modificar el original."""
    arr = list(datos)
    n = len(arr)
    izq = 0
    der = n - 1
    hubo_cambio = True
    while hubo_cambio:
        hubo_cambio = False
        k = izq
        for j in range(izq, der):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                k = j
                hubo_cambio = True
        der = k
        if not hubo_cambio:
            break
        hubo_cambio = False
        k = der
        for j in range(der - 1, izq - 1, -1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                k = j
                hubo_cambio = True
        izq = k
    return arr


def pasos(datos):
    """Generador para animación: emite (lista, evento, i, j) en cada paso."""
    arr = list(datos)
    n = len(arr)
    yield list(arr), "inicio", None, None
    pasada = 1
    izq = 0
    der = n - 1
    hubo_cambio = True
    while hubo_cambio:
        hubo_cambio = False
        k = izq
        yield list(arr), "pasada", pasada, "izq->der"
        for j in range(izq, der):
            yield list(arr), "comparar", j, j + 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                k = j
                hubo_cambio = True
                yield list(arr), "intercambiar", j, j + 1
        der = k
        if not hubo_cambio:
            break
        hubo_cambio = False
        k = der
        yield list(arr), "pasada", pasada + 0.5, "der->izq"
        for j in range(der - 1, izq - 1, -1):
            yield list(arr), "comparar", j, j + 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                k = j
                hubo_cambio = True
                yield list(arr), "intercambiar", j, j + 1
        izq = k
        pasada += 1
    yield list(arr), "fin", None, None