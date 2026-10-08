"""Ejercicio 3: depuracion y eliminacion de duplicados in-place.

Elimina los duplicados de un vector DESORDENADO conservando la
PRIMERA ocurrencia de cada valor. Los elementos se desplazan a la
izquierda sobre el propio vector original y se ajusta el tamano
logico efectivo; no se usa set(), dict(), sorted() ni ningun
arreglo auxiliar de tamano N (memoria O(1)).

Algoritmo: dos punteros sobre el mismo vector. `lectura` recorre
todo el original; `escrito` marca el tamano del tramo ya depurado.
Cada valor leido se compara contra todo el tramo [0, escrito): si es
nuevo se desplaza hacia la izquierda escribiendolo en `escrito`; si
ya aparecio se descarta y el puntero logico no avanza.
"""


def eliminar_duplicados(vector):
    """Depura el vector in-place y devuelve su nueva logica (tamano).

    Complejidad temporal: O(N^2) en el peor caso, ya que cada
    lectura compara contra todo el tramo ya depurado (requisito de
    no usar estructuras auxiliares sobre un vector desordenado).
    Complejidad espacial: O(1), solo dos indices de puntero.
    """
    escrito = 0  # tamano logico del tramo ya depurado
    for lectura in range(len(vector)):
        es_duplicado = False
        for j in range(escrito):
            if vector[j] == vector[lectura]:
                es_duplicado = True
                break

        if not es_duplicado:
            # se desplaza a la izquierda sobre el mismo vector
            vector[escrito] = vector[lectura]
            escrito += 1
        # si es duplicado simplemente se descarta: la lectura
        # siguiente ocupa la posicion basura que dejo atras
    return escrito


def leer_vector():
    """Lee N y N elementos por consola (sin ordenar).

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
    """Flujo completo: lectura, depuracion y verificacion."""
    print("ejercicio 3: eliminar duplicados in-place (primera ocurrencia)")
    vector = leer_vector()
    print(f"antes           : {vector}")
    logico = eliminar_duplicados(vector)
    print("despues (logico): ", end="")
    for i in range(logico):  # se imprime sin crear listas nuevas
        print(vector[i], end="" if i == logico - 1 else ", ")
    print()
    print(f"tamano efectivo : {logico} de {len(vector)} posiciones")


if __name__ == "__main__":
    main()
