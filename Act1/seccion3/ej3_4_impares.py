"""ejercicio 3.4: impresion recursiva de impares menores o iguales a n.

datos primitivos: un entero positivo leido por consola.
salida esperada: 1 3 5 7 9 para n igual a 10.
"""


def imprimir_impares(n):
    """imprime en consola los impares positivos menores o iguales que n.

    caso base: si n es menor o igual que cero, la funcion finaliza y no se
    imprime nada.
    caso inductivo: si n es mayor que cero, se resuelve la llamada con n - 1
    y al regresar de ella se imprime n cuando es impar.
    """
    if n <= 0:  # caso base
        return
    if n % 2 != 0:
        print(n, end=" ")
    # caso inductivo
    imprimir_impares(n - 1)


def main():
    """pide n por consola e imprime la secuencia de impares."""
    print("ejercicio 3.4: impresion recursiva de impares")
    n = int(input("ingrese n, entero positivo: "))
    imprimir_impares(n)
    print()


if __name__ == "__main__":
    main()
