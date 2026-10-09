"""ejercicio 3.2: potencia entera recursiva.

se eleva una base entera a una potencia entera no negativa usando solo el
operador de multiplicacion.

datos primitivos: una base entera y un exponente no negativo leidos por
consola.
salida esperada: potencia = 8 para la base 2 y el exponente 3.
"""


def potencia(a, n):
    """devuelve a elevado a la n usando solo multiplicaciones.

    caso base: si n vale cero, cualquier numero elevado a cero da uno, que es
    el elemento neutro de la multiplicacion.
    caso inductivo: si n es mayor que cero, el resultado es a multiplicado por
    a elevado a n - 1, de modo que el exponente baja de uno en uno.
    """
    if n == 0:  # caso base
        return 1
    # caso inductivo
    return a * potencia(a, n - 1)


def main():
    """pide la base y el exponente por consola y muestra la potencia."""
    print("ejercicio 3.2: potencia entera recursiva")
    a = int(input("ingrese la base entera: "))
    n = int(input("ingrese el exponente no negativo: "))
    resultado = potencia(a, n)
    print(f"potencia = {resultado}")


if __name__ == "__main__":
    main()
