"""ejercicio 2.2: funcion de ackermann.

definicion del enunciado:
    A(0, n) = n + 1                     cuando m vale cero
    A(m, 0) = A(m - 1, 1)               cuando m es mayor que cero y n vale cero
    A(m, n) = A(m - 1, A(m, n - 1))     cuando m es mayor que cero y n es mayor que cero

datos primitivos: dos enteros no negativos leidos por consola.
salida esperada: resultado = 4 para m igual a 1 y n igual a 2.
"""


def ackermann(m, n):
    """devuelve el valor de A(m, n).

    caso base: si m vale cero, la funcion se detiene y devuelve n + 1.
    caso inductivo: si m es mayor que cero y n vale cero, se reduce m en uno
    y se reinicia n en uno. si los dos son mayores que cero, primero se
    resuelve A(m, n - 1) y ese resultado se usa como segundo argumento de
    A(m - 1, ...).
    """
    if m == 0:  # caso base: unico punto donde la recursion se detiene
        return n + 1
    if n == 0:  # caso inductivo: se baja m en uno y se reinicia n en uno
        return ackermann(m - 1, 1)
    # caso inductivo: la llamada interna se resuelve antes de la externa
    interno = ackermann(m, n - 1)
    return ackermann(m - 1, interno)


def main():
    """pide m y n por consola y muestra el valor de A(m, n)."""
    print("ejercicio 2.2: funcion de ackermann")
    m = int(input("ingrese m, entero no negativo: "))
    n = int(input("ingrese n, entero no negativo: "))
    resultado = ackermann(m, n)
    print(f"resultado = {resultado}")


if __name__ == "__main__":
    main()
