"""ejercicio 3.8: impresion de los digitos separados por un espacio.

los digitos salen en el orden original, de izquierda a derecha, pero con un
espacio entre cada uno.

datos primitivos: un entero positivo leido por consola.
salida esperada: 4 5 6 7 para 4567.
"""


def imprimir_digitos_espaciados(n):
    """imprime en consola los digitos de n en orden y separados por espacio.

    caso base: si n es menor que diez, el numero tiene un solo digito y se
    imprime seguido de un espacio.
    caso inductivo: si n es mayor o igual que diez, primero se resuelve la
    llamada con la parte entera, que deja impresos los digitos de la
    izquierda, y al volver se imprime el digito de las unidades, que es el
    ultimo de la izquierda a la derecha.
    """
    if n < 10:  # caso base
        print(n, end=" ")
        return
    # caso inductivo
    imprimir_digitos_espaciados(n // 10)
    print(n % 10, end=" ")


def main():
    """pide el numero por consola e imprime sus digitos con espacio."""
    print("ejercicio 3.8: impresion de los digitos separados por espacio")
    n = int(input("ingrese un entero positivo: "))
    imprimir_digitos_espaciados(n)
    print()


if __name__ == "__main__":
    main()
