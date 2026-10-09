"""pruebas de la practica 1 de recursividad.

cubren los casos de prueba obligatorios de los ejercicios de la seccion 2 y de
la seccion 3, uno por metodo, sin usar listas ni tuplas para agrupar los casos.

ejecutar desde la carpeta act1 con:
    python -m unittest pruebas -v
"""

import unittest

from seccion2 import ej2_1_mcd, ej2_2_ackermann, ej2_3_particiones
from seccion3 import (
    ej3_1_multiplicacion,
    ej3_2_potencia,
    ej3_3_serie_armonica,
    ej3_6_cifras,
)


class TestMcd(unittest.TestCase):
    def test_caso_de_prueba_1(self):
        self.assertEqual(ej2_1_mcd.mcd(21, 154), 7)

    def test_caso_de_prueba_2(self):
        self.assertEqual(ej2_1_mcd.mcd(231, 182), 7)

    def test_cuando_el_segundo_parametro_es_cero(self):
        self.assertEqual(ej2_1_mcd.mcd(7, 0), 7)


class TestAckermann(unittest.TestCase):
    def test_caso_de_prueba_1(self):
        self.assertEqual(ej2_2_ackermann.ackermann(1, 2), 4)

    def test_caso_de_prueba_2(self):
        self.assertEqual(ej2_2_ackermann.ackermann(2, 2), 7)

    def test_caso_base_con_m_cero(self):
        self.assertEqual(ej2_2_ackermann.ackermann(0, 5), 6)


class TestParticiones(unittest.TestCase):
    def test_caso_de_prueba_1(self):
        self.assertEqual(ej2_3_particiones.particiones(5, 5), 7)

    def test_caso_de_prueba_2(self):
        self.assertEqual(ej2_3_particiones.particiones(6, 6), 11)

    def test_caso_base_con_m_igual_a_uno(self):
        self.assertEqual(ej2_3_particiones.particiones(1, 7), 1)


class TestSeccion3(unittest.TestCase):
    """pruebas de los ejercicios de la seccion 3 que devuelven un valor.

    los cuatro ejercicios que solo imprimen en consola, el 3.4, el 3.5, el
    3.7 y el 3.8, se comprueban con las capturas de evidencia del reporte,
    porque capturar la salida de la consola exigiria importar el modulo de
    cadenas de la biblioteca estandar y aqui no se admite ningun import
    distinto del de las pruebas.
    """

    def test_3_1_producto(self):
        self.assertEqual(ej3_1_multiplicacion.multiplicar(8, 3), 24)

    def test_3_1_producto_del_segundo_caso(self):
        self.assertEqual(ej3_1_multiplicacion.multiplicar(12, 5), 60)

    def test_3_2_potencia(self):
        self.assertEqual(ej3_2_potencia.potencia(2, 3), 8)

    def test_3_2_potencia_del_segundo_caso(self):
        self.assertEqual(ej3_2_potencia.potencia(5, 4), 625)

    def test_3_3_serie_armonica_de_un_termino(self):
        self.assertAlmostEqual(ej3_3_serie_armonica.serie_armonica(1), 1.0)

    def test_3_3_serie_armonica_de_cuatro_terminos(self):
        self.assertAlmostEqual(
            ej3_3_serie_armonica.serie_armonica(4), 2.08333, places=5
        )

    def test_3_6_cifras(self):
        self.assertEqual(ej3_6_cifras.contar_digitos(7654), 4)

    def test_3_6_cifras_de_un_solo_digito(self):
        self.assertEqual(ej3_6_cifras.contar_digitos(9), 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
