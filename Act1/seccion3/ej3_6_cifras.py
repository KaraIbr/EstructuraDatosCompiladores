"""ejercicio 3.6: conteo recursivo de las cifras de un entero.

la cantidad de digitos se obtiene dividiendo el numero entre diez en cada
llamada, hasta que solo quede un digito.

datos primitivos: un entero positivo leido por consola.
salida esperada: cifras = 4 para 7654.
"""


def contar_digitos(n):
    """devuelve cuantos digitos compose el entero n.

    caso base: si n es menor que diez, el numero tiene un solo digito y se
    devuelve uno.
    caso inductivo: si n es mayor o igual que diez, se cuenta el digito de las
    unidades y se suman las cifras que tiene la division entera entre diez,
    que es un numero mas corto.
    """
    if n < 10:  # caso base
        return 1
    # caso inductivo
    return 1 + contar_digitos(n // 10)


def main():
    """pide el numero por consola y muestra cuantas cifras tiene."""
    print("ejercicio 3.6: conteo recursivo de cifras de un entero")
    n = int(input("ingrese un entero positivo: "))
    total = contar_digitos(n)
    print(f"cifras = {total}")


if __name__ == "__main__":
    main()
