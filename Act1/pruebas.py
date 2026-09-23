"""pruebas de la practica 1 de recursividad.

cubren los casos de prueba obligatorios de los ejercicios de la seccion 2 y de
la seccion 3, uno por metodo, sin usar listas ni tuplas para agrupar los casos.

ejecutar desde la carpeta act1 con:
    python -m unittest pruebas -v
"""

import unittest

from seccion2 import ej2_1_mcd, ej2_2_ackermann, ej2_3_particiones


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


if __name__ == "__main__":
    unittest.main(verbosity=2)
