"""Ejercicio 4: subarreglo contiguo de suma maxima (Kadane).

Dado un vector con positivos y negativos, identifica la suma mas
alta posible entre TODOS los subarreglos contiguos e imprime la
suma maxima, el subarreglo optimo y sus indices de inicio y fin.

Algoritmo: Kadane con reinicio. Se acumula una suma en curso; si
cae por debajo de cero se reinicia porque un prefijo negativo nunca
puede mejorar a un subarreglo que empiece mas adelante.
"""


def kadane(vector):
    """Devuelve (suma_maxima, inicio, fin) del mejor subarreglo contiguo.

    Complejidad temporal: O(N), un unico recorrido lineal.
    Complejidad espacial: O(1), tres indices y dos acumuladores.
    """
    # el vector se asume con al menos un elemento (valida main)
    suma_maxima = vector[0]
    suma_actual = vector[0]
    inicio_mejor = 0
    fin_mejor = 0
    inicio_actual = 0

    for i in range(1, len(vector)):
        if suma_actual < 0:
            # un prefijo negativo no conviene: se reinicia aqui
            suma_actual = vector[i]
            inicio_actual = i
        else:
            suma_actual += vector[i]

        if suma_actual > suma_maxima:
            suma_maxima = suma_actual
            inicio_mejor = inicio_actual
            fin_mejor = i

    return suma_maxima, inicio_mejor, fin_mejor


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
    """Flujo completo: lectura, aplicacion de Kadane y reporte."""
    print("ejercicio 4: subarreglo contiguo de suma maxima (Kadane)")
    vector = leer_vector()

    suma, inicio, fin = kadane(vector)
    print(f"suma maxima : {suma}")
    print(f"indice inicio: {inicio}")
    print(f"indice fin   : {fin}")
    print("subarreglo   : [", end="")
    for i in range(inicio, fin + 1):
        print(vector[i], end="" if i == fin else ", ")
    print("]")


if __name__ == "__main__":
    main()
