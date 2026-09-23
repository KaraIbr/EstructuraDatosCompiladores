"""ejercicio 2.1: maximo comun divisor con el algoritmo de euclides.

definicion del enunciado:
    mcd(m, n) = mcd(n, m % n)   cuando n es mayor que cero
    mcd(m, 0) = m                cuando n es igual a cero

datos primitivos: dos enteros positivos leidos por consola.
salida esperada: mcd = 7 para la entrada 21 y 154.
"""


def mcd(m, n):
    """devuelve el maximo comun divisor de m y n.

    caso base: si n vale cero, el dividendo ya es multiplo del otro numero
    y se devuelve directamente.
    caso inductivo: si n es mayor que cero, el mismo problema se resuelve
    con el residuo de dividir m entre n, pasando n como nuevo primer
    operando para que el segundo operando siempre baje.
    """
    if n == 0:  # caso base
        return m
    # caso inductivo
    return mcd(n, m % n)


def main():
    """pide los dos operandos por consola y muestra el resultado."""
    print("ejercicio 2.1: maximo comun divisor por el algoritmo de euclides")
    m = int(input("ingrese el primer entero positivo: "))
    n = int(input("ingrese el segundo entero positivo: "))
    resultado = mcd(m, n)
    print(f"mcd = {resultado}")


if __name__ == "__main__":
    main()
