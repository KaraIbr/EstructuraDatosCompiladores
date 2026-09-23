"""ejercicio 2.3: particiones de un entero.

esquema del enunciado:
    P(1, n) = 1                         para todo n
    P(m, 1) = 1                         para todo m
    P(m, n) = P(m, m)                   si m es menor que n
    P(m, n) = 1 + P(m, m - 1)           si m es igual que n
    P(m, n) = P(m, n - 1) + P(m - n, n) si m es mayor que n

para obtener todas las particiones de un entero x se llama con m igual a x y
n igual a x.

datos primitivos: dos enteros positivos leidos por consola.
salida esperada: total de particiones = 7 para m igual a 5 y n igual a 5.
"""


def particiones(m, n):
    """devuelve cuantas formas hay de escribir m como suma de 1 hasta n.

    caso base: si m vale 1 o si n vale 1 hay una unica forma, se devuelve 1.
    caso inductivo: si m es menor que n el limite superior se ajusta a m; si
    m es igual que n se cuenta la forma que usa solo m y se suman las que no
    lo usan; si m es mayor que n se suman las particiones que no usan n con
    las que usan al menos un n.
    """
    if m == 1 or n == 1:  # caso base
        return 1
    if m < n:  # caso inductivo
        return particiones(m, m)
    if m == n:  # caso inductivo
        return 1 + particiones(m, m - 1)
    # caso inductivo
    return particiones(m, n - 1) + particiones(m - n, n)


def main():
    """pide m y n por consola y muestra el total de particiones."""
    print("ejercicio 2.3: particiones de un entero")
    m = int(input("ingrese m, entero positivo: "))
    n = int(input("ingrese n, entero positivo: "))
    total = particiones(m, n)
    print(f"total de particiones = {total}")


if __name__ == "__main__":
    main()
