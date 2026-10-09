"""ejercicio 3.3: suma de la serie armonica.

1/1 + 1/2 + 1/3 + 1/4 + ... + 1/n

datos primitivos: un entero positivo leido por consola.
salida esperada: suma = 2.08333 para n igual a 4.
"""


def serie_armonica(n):
    """devuelve la suma de los primeros n terminos de la serie armonica.

    caso base: si n vale cero o es negativo, no queda ningun termino por
    sumar y la suma acumulada es cero.
    caso inductivo: si n es mayor que cero, la suma es 1/n mas la suma de los
    primeros n - 1 terminos, de modo que el limite baja de uno en uno hasta
    el caso base.
    """
    if n <= 0:  # caso base
        return 0.0
    # caso inductivo
    return 1 / n + serie_armonica(n - 1)


def main():
    """pide n por consola y muestra la suma con cinco decimales."""
    print("ejercicio 3.3: suma de la serie armonica")
    n = int(input("ingrese n, entero positivo: "))
    suma = serie_armonica(n)
    print(f"suma = {suma:.5f}")


if __name__ == "__main__":
    main()
