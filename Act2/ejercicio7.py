"""Ejercicio 7: tabla de frecuencias e histograma grafico.

Calcula la frecuencia absoluta de valores discretos comprendidos
entre 1 y 5 (por ejemplo calificaciones) y la imprime como una
tabla seguida de un histograma de barras horizontales formateado
con asteriscos (*), un asterisco por unidad de frecuencia.

La tabla de conteo usa un arreglo de R = 5 posiciones fijo, no un
arreglo auxiliar de tamano N.
"""

RANGO_INFERIOR = 1
RANGO_SUPERIOR = 5


def calcular_frecuencias(vector):
    """Devuelve la tabla de frecuencias absolutas del rango 1..5.

    Complejidad temporal: O(N + R) -> N para contar y R para
    formar la tabla (R = 5, rango fijo del ejercicio).
    Complejidad espacial: O(R), solo cinco contadores, indepen-
    diente del tamano N del vector.
    """
    tabla = [0] * (RANGO_SUPERIOR - RANGO_INFERIOR + 1)
    for valor in vector:
        tabla[valor - RANGO_INFERIOR] += 1
    return tabla


def imprimir_histograma(tabla):
    """Imprime la tabla de frecuencias y las barras de asteriscos.

    Complejidad temporal: O(R + F) donde F es la frecuencia total
    (cada asterisco se imprime una vez).
    Complejidad espacial: O(1), solo variables de formato.
    """
    total = sum(tabla)
    print("\nfrecuencias absolutas")
    print("valor | frec. | porcentaje | histograma")
    print("------+------+------------+------------------")
    for indice, frecuencia in enumerate(tabla):
        valor = RANGO_INFERIOR + indice
        porcentaje = (frecuencia * 100) / total if total else 0
        barras = "*" * frecuencia
        print(f"  {valor}   |  {frecuencia:3d}  |   {porcentaje:5.1f} %  | {barras}")
    print(f"total |  {total:3d}  |    100.0 %  |")


def leer_vector():
    """Lee N y N valores discretos validados dentro del rango 1..5.

    Complejidad temporal: O(N). Complejidad espacial: O(N), la
    entrada que pide el enunciado.
    """
    n = int(input("tamano N del vector: "))
    while n <= 0:
        print("N debe ser mayor que cero.")
        n = int(input("tamano N del vector: "))
    vector = []
    for i in range(n):
        valor = int(input(f"elemento [{i}] ({RANGO_INFERIOR}..{RANGO_SUPERIOR}): "))
        while valor < RANGO_INFERIOR or valor > RANGO_SUPERIOR:
            print(f"  valor fuera de rango, use {RANGO_INFERIOR}..{RANGO_SUPERIOR}.")
            valor = int(input(f"elemento [{i}]: "))
        vector.append(valor)
    return vector


def main():
    """Flujo completo: lectura, conteo y despliegue del histograma."""
    print("ejercicio 7: tabla de frecuencias e histograma con asteriscos")
    vector = leer_vector()
    tabla = calcular_frecuencias(vector)
    imprimir_histograma(tabla)


if __name__ == "__main__":
    main()
