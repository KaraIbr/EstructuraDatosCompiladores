"""Ejercicio 9: producto cruzado sin operador de division.

Dado el vector A, construye el vector B donde B[i] es el producto
de TODOS los elementos de A excepto A[i].

RESTRICCION OBLIGATORIA: queda prohibido el operador de division
('/'). La solucion recorre A una sola vez acumulando productos de
PREFIJOS dentro de B y luego una pasada de DERECHA A IZQUIERDA
acumulando productos de SUFIJOS.

    B[i] = (producto de A[0..i-1]) * (producto de A[i+1..N-1])
"""


def producto_cruzado(a):
    """Devuelve B con el producto de todos los elementos menos A[i].

    Complejidad temporal: O(N) -> dos recorridos lineales sobre A.
    Complejidad espacial: O(1) auxiliar -> unicamente dos variables
    acumuladoras; el vector B es la salida pedida por el enunciado.
    """
    n = len(a)
    b = [1] * n

    # pasada 1: productos de prefijos, de izquierda a derecha
    acumulado = 1
    for i in range(n):
        b[i] = acumulado          # guarda producto de A[0..i-1]
        acumulado *= a[i]

    # pasada 2: productos de sufijos, de derecha a izquierda,
    # multiplicados en el lugar sobre el prefijo ya guardado
    acumulado = 1
    for i in range(n - 1, -1, -1):
        b[i] *= acumulado         # ahora tiene prefijo * sufijo
        acumulado *= a[i]

    return b


def verificar(a, b):
    """Recalcula B[i] con multiplicaciones anidadas (sin division).

    Complejidad temporal: O(N^2) -> solo con fines de verificacion
    en pantalla; el algoritmo real del ejercicio es O(N).
    Complejidad espacial: O(1).
    """
    for i in range(len(a)):
        producto = 1
        for j in range(len(a)):
            if j != i:
                producto *= a[j]
        if producto != b[i]:
            return False
    return True


def leer_vector():
    """Lee N y N elementos por consola.

    Complejidad temporal: O(N). Complejidad espacial: O(N), la
    entrada que pide el enunciado.
    """
    n = int(input("tamano N del vector A: "))
    while n <= 0:
        print("N debe ser mayor que cero.")
        n = int(input("tamano N del vector A: "))
    vector = []
    for i in range(n):
        vector.append(int(input(f"  A[{i}]: ")))
    return vector


def main():
    """Flujo completo: lectura, producto cruzado y verificacion."""
    print("ejercicio 9: producto cruzado sin usar el operador '/'")
    a = leer_vector()

    b = producto_cruzado(a)
    print(f"A = {a}")
    print(f"B = {b}")
    for i in range(len(b)):
        print(f"  B[{i}] = {b[i]}")

    if verificar(a, b):
        print("verificacion por multiplicacion directa: correcta "
              "(sin divisiones en todo el programa)")


if __name__ == "__main__":
    main()
