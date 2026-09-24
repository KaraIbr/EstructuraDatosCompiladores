"""Pruebas exhaustivas de los cinco métodos de ordenación (Unidad 2).

Cubre el criterio 4 de la rúbrica: verificar que cada método ordena
correctamente con distintos tipos de arreglos, sin modificar la
entrada y respetando sus invariantes de conteo.

Ejecutar con:
    python -m unittest tests -v
"""

import random
import unittest

from metodos import burbuja, burbuja_senal, sacudida, insercion, seleccion

METODOS = [
    ("burbuja", burbuja),
    ("burbuja_con_senal", burbuja_senal),
    ("sacudida", sacudida),
    ("insercion_directa", insercion),
    ("seleccion_directa", seleccion),
]


def construir_casos():
    """Devuelve un diccionario de casos de prueba representativos."""
    rnd = random.Random(42)
    casi = list(range(40))
    rnd2 = random.Random(7)
    for _ in range(8):
        a, b = rnd2.sample(range(40), 2)
        casi[a], casi[b] = casi[b], casi[a]
    return {
        "vacio": [],
        "un_elemento": [3],
        "ordenado": list(range(40)),
        "inverso": list(range(40, 0, -1)),
        "aleatorio": [rnd.randint(-100, 100) for _ in range(60)],
        "casi_ordenado": casi,
        "duplicados": [5, 3, 5, 2, 3, 5, 2, 2, 7, 3] * 4,
        "negativos": [-12, -5, 0, 3, -99, 12, -1],
    }


def contar_eventos(mod, datos):
    """Cuenta comparaciones, intercambios/desplazamientos y pasadas."""
    comp = mov = pas = 0
    for _arr, evento, _i, _j in mod.pasos(datos):
        if evento == "comparar":
            comp += 1
        elif evento in ("intercambiar", "desplazar"):
            mov += 1
        elif evento == "pasada":
            pas += 1
    return comp, mov, pas


class TestCorrectitud(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.casos = construir_casos()

    def test_ordenar_coincide_con_sorted(self):
        for nombre, mod in METODOS:
            for tipo, datos in self.casos.items():
                with self.subTest(metodo=nombre, caso=tipo):
                    self.assertEqual(mod.ordenar(datos), sorted(datos))

    def test_preserva_longitud(self):
        for nombre, mod in METODOS:
            for tipo, datos in self.casos.items():
                with self.subTest(metodo=nombre, caso=tipo):
                    self.assertEqual(len(mod.ordenar(datos)), len(datos))

    def test_no_modifica_la_entrada(self):
        for nombre, mod in METODOS:
            for tipo, datos in self.casos.items():
                with self.subTest(metodo=nombre, caso=tipo):
                    original = list(datos)
                    mod.ordenar(datos)
                    self.assertEqual(datos, original)

    def test_generador_pasos_termina_ordenado(self):
        for nombre, mod in METODOS:
            for tipo, datos in self.casos.items():
                with self.subTest(metodo=nombre, caso=tipo):
                    pasos = list(mod.pasos(datos))
                    self.assertEqual(pasos[0][1], "inicio")
                    self.assertEqual(pasos[-1][1], "fin")
                    self.assertEqual(pasos[-1][0], sorted(datos))

    def test_fuzz_aleatorio(self):
        rnd = random.Random(2026)
        for _ in range(40):
            n = rnd.randint(0, 30)
            datos = [rnd.randint(-50, 50) for _ in range(n)]
            for _nombre, mod in METODOS:
                with self.subTest(n=n, metodo=_nombre):
                    self.assertEqual(mod.ordenar(datos), sorted(datos))


class TestInvariantesDeConteo(unittest.TestCase):
    def test_burbuja_siempre_compara_n_al_cuadrado_medios(self):
        n = 25
        comp, _mov, pas = contar_eventos(burbuja, list(range(n, 0, -1)))
        self.assertEqual(comp, n * (n - 1) // 2)
        self.assertEqual(pas, n - 1)

    def test_seleccion_siempre_compara_n_al_cuadrado_medios(self):
        n = 25
        datos = [random.Random(1).randint(0, 100) for _ in range(n)]
        comp, mov, pas = contar_eventos(seleccion, datos)
        self.assertEqual(comp, n * (n - 1) // 2)
        self.assertEqual(pas, n - 1)
        self.assertLessEqual(mov, n - 1)

    def test_burbuja_con_senal_adaptativa_en_ordenado(self):
        n = 30
        comp, mov, pas = contar_eventos(burbuja_senal, list(range(n)))
        self.assertEqual(comp, n - 1)
        self.assertEqual(mov, 0)

    def test_insercion_sin_movimientos_en_ordenado(self):
        n = 30
        comp, mov, _pas = contar_eventos(insercion, list(range(n)))
        self.assertEqual(comp, n - 1)
        self.assertEqual(mov, 0)

    def test_sacudida_adaptativa_en_ordenado(self):
        n = 30
        comp, mov, _pas = contar_eventos(sacudida, list(range(n)))
        self.assertEqual(comp, n - 1)
        self.assertEqual(mov, 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)