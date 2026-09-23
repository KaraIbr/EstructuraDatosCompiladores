"""ejercicio 3.1: multiplicacion recursiva mediante sumas.

el producto de dos enteros positivos se obtiene solo con sumas, sin usar el
operador de multiplicacion.

datos primitivos: dos enteros positivos leidos por consola.
salida esperada: producto = 24 para 8 y 3.
"""


def multiplicar(m, n):
    """devuelve el producto de m y n usando unicamente sumas.

    caso base: si n vale cero, cualquier cantidad multiplicada por cero da
    cero, y no queda nada por sumar.
    caso inductivo: si n es mayor que cero, el producto es m mas el producto
    de m por n - 1, con lo cual la segunda cantidad baja de uno en uno hasta
    llegar al caso base.
    """
    if n == 0:  # caso base
        return 0
    # caso inductivo
    return m + multiplicar(m, n - 1)


def main():
    """pide los dos factores por consola y muestra el producto."""
    print("ejercicio 3.1: multiplicacion recursiva mediante sumas")
    m = int(input("ingrese el primer entero positivo: "))
    n = int(input("ingrese el segundo entero positivo: "))
    producto = multiplicar(m, n)
    print(f"producto = {producto}")


if __name__ == "__main__":
    main()
