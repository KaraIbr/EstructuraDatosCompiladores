"""Ejercicio 6: picos locales y elemento mayoritario (Boyer-Moore).

Subproblema 1: identificar los picos locales, es decir los elementos
mayores que sus vecinos inmediatos (los extremos comparan solo con
el unico vecino que tienen).

Subproblema 2: algoritmo de Votacion de Boyer-Moore para verificar
si existe un numero con frecuencia estrictamente mayor que
piso(N/2). Dos fases: candidato y verificacion, ambas sin tablas
auxiliares (memoria O(1)).
"""


def picos_locales(vector):
    """Devuelve la lista de indices que son picos locales.

    Complejidad temporal: O(N), un recorrido lineal de vecinos.
    Complejidad espacial: O(1) auxiliar; la lista devuelta solo
    almacena los picos encontrados (como maximo N/2 indices).
    """
    n = len(vector)
    if n == 0:
        return []
    if n == 1:
        return [0]  # sin vecinos, se considera pico trivial

    picos = []
    for i in range(n):
        if i == 0:
            es_pico = vector[i] > vector[i + 1]
        elif i == n - 1:
            es_pico = vector[i] > vector[i - 1]
        else:
            es_pico = vector[i] > vector[i - 1] and vector[i] > vector[i + 1]
        if es_pico:
            picos.append(i)
    return picos


def mayoria_boyer_moore(vector):
    """Busca el elemento mayoritario (frecuencia > piso(N/2)).

    Fase 1 (candidato): un contador sube con el candidato actual y
    baja con cualquier distinto; al terminar, si hay mayoria, su
    elemento sobrevive como candidato.
    Fase 2 (verificacion): se recuenta el candidato para confirmar
    que supera piso(N/2).

    Complejidad temporal: O(N) -> dos recorridos lineales.
    Complejidad espacial: O(1) -> un candidato y un contador.
    """
    candidato = None
    contador = 0

    # fase 1: votacion
    for valor in vector:
        if contador == 0:
            candidato = valor
            contador = 1
        elif valor == candidato:
            contador += 1
        else:
            contador -= 1

    # fase 2: verificacion de la frecuencia real
    frecuencia = 0
    for valor in vector:
        if valor == candidato:
            frecuencia += 1

    if candidato is not None and frecuencia > len(vector) // 2:
        return candidato, frecuencia
    return None, frecuencia


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
    """Flujo completo: lectura, picos locales y votacion de mayoria."""
    print("ejercicio 6: picos locales y elemento mayoritario (Boyer-Moore)")
    vector = leer_vector()

    indices = picos_locales(vector)
    if indices:
        print("picos locales:")
        for i in indices:
            print(f"  indice [{i}] -> {vector[i]}")
    else:
        print("no hay picos locales en el vector.")

    mayoria, frecuencia = mayoria_boyer_moore(vector)
    if mayoria is None:
        print(f"no hay elemento mayoritario (maxima frecuencia {frecuencia}"
              f" de {len(vector)}, umbral {len(vector) // 2})")
    else:
        print(f"mayoritario: {mayoria} con frecuencia {frecuencia}"
              f" de {len(vector)} (> {len(vector) // 2})")


if __name__ == "__main__":
    main()
