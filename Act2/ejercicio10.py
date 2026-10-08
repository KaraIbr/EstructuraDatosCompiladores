"""Ejercicio 10: subarreglo contiguo mas largo con suma objetivo K.

Encuentra la longitud maxima, el subarreglo y el rango de indices
cuya suma sea exactamente K.

Algoritmo: acumulacion de SUMA PREFIJA con registro de la PRIMERA
aparicion de cada valor de prefijo en un diccionario. Si en la
posicion i la suma es S, cualquier prefixo previo con valor S-K
identifica un subarreglo de suma K cuyo indice inicial es
primera_aparicion[S-K] + 1. Registrar solo la primera aparicion
garantiza la mayor longitud posible y un recorrido unico O(N).
"""


def subarreglo_suma_k(vector, k):
    """Devuelve (longitud, inicio, fin) del subarreglo mas largo con suma k.

    Complejidad temporal: O(N) -> un unico recorrido lineal; cada
    consulta de prefijo es O(1) amortizado en el diccionario.
    Complejidad espacial: O(N) -> el diccionario almacena como
    maximo un registro distinto por posicion del vector.
    """
    primera_ocurrencia = {0: -1}  # prefijo nulo antes de empezar
    suma = 0
    mejor_longitud = 0
    mejor_inicio = -1
    mejor_fin = -1

    for i in range(len(vector)):
        suma += vector[i]  # suma prefija que termina en i

        prefijo_objetivo = suma - k
        if prefijo_objetivo in primera_ocurrencia:
            inicio = primera_ocurrencia[prefijo_objetivo] + 1
            longitud = i - inicio + 1  # el rango es cerrado [inicio..i]
            if longitud > mejor_longitud:
                mejor_longitud = longitud
                mejor_inicio = inicio
                mejor_fin = i

        # solo la PRIMERA aparicion: no se sobrescribe nunca
        if suma not in primera_ocurrencia:
            primera_ocurrencia[suma] = i

    return mejor_longitud, mejor_inicio, mejor_fin


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
    """Flujo completo: lectura, busqueda O(N) y reporte."""
    print("ejercicio 10: subarreglo contiguo mas largo con suma exacta K")
    vector = leer_vector()
    k = int(input("valor objetivo K: "))

    longitud, inicio, fin = subarreglo_suma_k(vector, k)
    if longitud == 0:
        print(f"no existe ningun subarreglo contiguo con suma exacta {k}.")
        return

    print(f"longitud maxima: {longitud}")
    print(f"rango de indices: [{inicio} .. {fin}]")
    print("subarreglo: [", end="")
    for i in range(inicio, fin + 1):
        print(vector[i], end="" if i == fin else ", ")
    print("]")


if __name__ == "__main__":
    main()
