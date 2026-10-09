"""ejercicio 3.7: impresion inversa de los digitos de un numero.

los digitos salen de derecha a izquierda usando el residuo de dividir entre
diez y la division entera.

datos primitivos: un entero positivo leido por consola.
salida esperada: 7654 para 4567.
"""


def imprimir_digitos_inversos(n):
    """imprime en consola los digitos de n al reves, sin separador.

    caso base: si n es menor que diez, el numero tiene un solo digito y se
    imprime directamente.
    caso inductivo: si n es mayor o igual que diez, se imprime primero el
    residuo de la division entre diez, que es el digito de la derecha, y
    despues se resuelve la llamada con la parte entera, que trae los digitos
    que faltan en el mismo orden invertido.
    """
    if n < 10:  # caso base
        print(n, end="")
        return
    # caso inductivo
    print(n % 10, end="")
    imprimir_digitos_inversos(n // 10)


def main():
    """pide el numero por consola e imprime sus digitos al reves."""
    print("ejercicio 3.7: impresion inversa de los digitos de un numero")
    n = int(input("ingrese un entero positivo: "))
    imprimir_digitos_inversos(n)
    print()


if __name__ == "__main__":
    main()
