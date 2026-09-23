"""pruebas de la practica 1 de recursividad.

cubren los casos de prueba obligatorios de los ejercicios de la seccion 2 y de
la seccion 3, uno por metodo, sin usar listas ni tuplas para agrupar los casos.

ejecutar desde la carpeta act1 con:
    python -m unittest pruebas -v
"""

import unittest

from seccion2 import ej2_1_mcd


class TestMcd(unittest.TestCase):
    def test_caso_de_prueba_1(self):
        self.assertEqual(ej2_1_mcd.mcd(21, 154), 7)

    def test_caso_de_prueba_2(self):
        self.assertEqual(ej2_1_mcd.mcd(231, 182), 7)

    def test_cuando_el_segundo_parametro_es_cero(self):
        self.assertEqual(ej2_1_mcd.mcd(7, 0), 7)


if __name__ == "__main__":
    unittest.main(verbosity=2)
