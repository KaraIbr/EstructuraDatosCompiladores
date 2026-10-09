"""ejercicio 3.5: inversion de una sucesion leida por consola.

los datos no se guardan en ninguna estructura: la pila de llamadas hace de
almacen. el cero es la bandera que marca el fin de la entrada.

datos primitivos: enteros positivos leidos por consola hasta el cero.
salida esperada: la secuencia invertida, por ejemplo 2 9 4 para 4 9 2 0.
"""


def invertir():
    """lee un entero, se llama a si misma y al volver imprime el que leyo.

    caso base: si el entero leido es cero, no se hace ninguna llamada mas y
    empieza el desapilamiento.
    caso inductivo: si el entero leido es distinto de cero, primero se
    resuelve la llamada interna, que lee el siguiente dato, y solo despues se
    imprime el valor que quedo guardado en este marco de pila.
    """
    x = int(input("ingrese un entero positivo, cero termina: "))
    if x == 0:  # caso base
        return
    # caso inductivo
    invertir()
    print(x, end=" ")


def main():
    """pide la sucesion terminada en cero e imprime la secuencia invertida."""
    print("ejercicio 3.5: inversion de una sucesion leida por consola")
    invertir()
    print()


if __name__ == "__main__":
    main()
