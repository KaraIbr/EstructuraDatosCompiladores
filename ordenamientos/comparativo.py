"""Comparativo de los cinco métodos de ordenación (Unidad 2).

Corre los cinco algoritmos sobre los mismos datos y muestra las
comparaciones, intercambios, pasadas y tiempo de ejecución.

Uso:
    python comparativo.py            # modo gráfico (barras lado a lado)
    python comparativo.py --texto    # tabla en la consola
"""

import random
import sys
import time
import tkinter as tk
from tkinter import ttk

from metodos import burbuja, burbuja_senal, sacudida, insercion, seleccion

METODOS = [
    ("Burbuja", burbuja),
    ("Burbuja con señal", burbuja_senal),
    ("Sacudida", sacudida),
    ("Inserción directa", insercion),
    ("Selección directa", seleccion),
]

TIPOS = ["aleatorio", "ordenado", "inverso", "casi_ordenado", "duplicados"]
N = 35
REP = 10


def generar_datos(tipo, n):
    """Devuelve una lista de n valores según el tipo solicitado."""
    base = list(range(10, 10 + n * 3, 3))
    if tipo == "ordenado":
        return base
    if tipo == "inverso":
        return list(reversed(base))
    if tipo == "casi_ordenado":
        datos = base[:]
        for _ in range(max(1, n // 5)):
            a, b = random.sample(range(n), 2)
            datos[a], datos[b] = datos[b], datos[a]
        return datos
    if tipo == "duplicados":
        return [random.randint(10, 80) for _ in range(n)]
    random.shuffle(base)
    return base


def metricas(mod, datos):
    """Cuenta comparaciones/intercambios/pasadas y mide el tiempo real."""
    comparaciones = intercambios = pasadas = 0
    for _arr, evento, _i, _j in mod.pasos(datos):
        if evento == "comparar":
            comparaciones += 1
        elif evento in ("intercambiar", "desplazar"):
            intercambios += 1
        elif evento == "pasada":
            pasadas += 1
    t0 = time.perf_counter()
    for _ in range(REP):
        mod.ordenar(datos)
    tiempo = (time.perf_counter() - t0) / REP * 1000
    return comparaciones, intercambios, pasadas, tiempo


def modo_texto():
    random.seed(11)
    datos = generar_datos("aleatorio", 50)
    print(f"Dataset: aleatorio con {len(datos)} elementos "
          f"(promedio de {REP} corridas)\n")
    print(f"{'Método':<20}{'Compar':>9}{'Interc':>9}{'Pasadas':>9}{'Tiempo (ms)':>12}")
    print("-" * 62)
    for nombre, mod in METODOS:
        c, it, p, t = metricas(mod, datos)
        print(f"{nombre:<20}{c:>9}{it:>9}{p:>9}{t:>12.4f}")


class Comparativo:
    def __init__(self, root):
        self.root = root
        root.title("Comparativo de los cinco métodos de ordenación")
        root.configure(bg="#1e1e2e")

        self.n = N
        self.tipo = "aleatorio"
        self.datos = generar_datos(self.tipo, self.n)
        self.pasos = [list(m.pasos(self.datos)) for _n, m in METODOS]
        self.indices = [0] * len(METODOS)
        self.terminados = [False] * len(METODOS)
        self.corre = False

        self._crear_toolbar()
        self._crear_pistas()
        self._crear_tabla()

    def _crear_toolbar(self):
        bar = ttk.Frame(self.root, padding=6)
        bar.pack(fill="x")
        ttk.Label(bar, text="Datos:").pack(side="left")
        self.tipo_var = tk.StringVar(value="aleatorio")
        for t in TIPOS:
            ttk.Radiobutton(bar, text=t.replace("_", " "), value=t,
                            variable=self.tipo_var,
                            command=self._cambiar_datos).pack(side="left", padx=2)
        ttk.Label(bar, text="  Elementos:").pack(side="left")
        self.tam = ttk.Spinbox(bar, from_=15, to=60, width=4)
        self.tam.pack(side="left", padx=2)
        ttk.Button(bar, text="▶ Correr", command=self._correr).pack(side="left", padx=8)
        ttk.Button(bar, text="Mezclar", command=self._cambiar_datos).pack(side="left")
        self.estado = ttk.Label(bar, text="Listo", font=("Segoe UI", 9, "bold"))
        self.estado.pack(side="right")

    def _crear_pistas(self):
        cont = ttk.Frame(self.root)
        cont.pack(fill="both", expand=True)
        self.canvases = []
        for nombre, _m in METODOS:
            col = ttk.Frame(cont)
            col.pack(side="left", fill="both", expand=True, padx=2, pady=2)
            ttk.Label(col, text=nombre, font=("Segoe UI", 9, "bold")).pack()
            cv = tk.Canvas(col, width=150, height=320, bg="#11111b", highlightthickness=0)
            cv.pack(fill="both", expand=True)
            self.canvases.append(cv)
        self._dibujar_todos()

    def _crear_tabla(self):
        self.tabla = tk.Text(self.root, height=9, font=("Consolas", 9),
                             bg="#1e1e2e", fg="#cdd6f4", state="normal")
        self.tabla.pack(fill="x", padx=6, pady=6)

    def _cambiar_datos(self):
        if self.corre:
            return
        t = self.tipo = self.tipo_var.get()
        try:
            self.n = int(self.tam.get())
        except (ValueError, tk.TclError):
            self.n = N
        self.datos = generar_datos(t, self.n)
        self.pasos = [list(m.pasos(self.datos)) for _n, m in METODOS]
        self.indices = [0] * len(METODOS)
        self.terminados = [False] * len(METODOS)
        self.tabla.delete("1.0", "end")
        self.estado.config(text="Listo")
        self._dibujar_todos()

    def _correr(self):
        if self.corre:
            return
        self.corre = True
        self.estado.config(text="Corriendo...")
        self._tick()

    def _tick(self):
        todos = True
        for k, (_nombre, mod) in enumerate(METODOS):
            if self.terminados[k]:
                continue
            idx = self.indices[k]
            if idx < len(self.pasos[k]):
                _arr, evento, _i, _j = self.pasos[k][idx]
                self.indices[k] += 1
                self._dibujar_carril(k, evento)
            else:
                self.terminados[k] = True
                self._dibujar_carril(k, "fin")
            todos = todos and self.terminados[k]
        if todos:
            self.corre = False
            self.estado.config(text="Terminado ✔")
            self._mostrar_resumen()
            return
        self.root.after(8, self._tick)

    def _dibujar_carril(self, k, evento):
        cv = self.canvases[k]
        arr = self.pasos[k][min(self.indices[k], len(self.pasos[k]) - 1)][0]
        cv.delete("all")
        n = len(arr)
        ancho, alto = cv.winfo_width() or 150, cv.winfo_height() or 300
        margen = 6
        maxv = max(arr, default=1)
        bar_w = max(1, (ancho - margen) / n)
        for pos, v in enumerate(arr):
            h = v / maxv * (alto - 40)
            color = "#89b4fa"
            if evento == "comparar" and pos in (self.indices[k], self.indices[k] + 1):
                color = "#f38ba8"
            cv.create_rectangle(pos * bar_w + margen // 2, alto - h,
                                pos * bar_w + bar_w + margen // 2, alto,
                                fill=color, outline="")

    def _dibujar_todos(self):
        for k in range(len(METODOS)):
            self._dibujar_carril(k, "inicio")

    def _mostrar_resumen(self):
        filas = [f"{'Método':<20}{'Compar':>9}{'Interc':>9}{'Pasadas':>9}{'Tiempo (ms)':>12}",
                 "-" * 62]
        for _nombre, mod in METODOS:
            c, it, p, t = metricas(mod, self.datos)
            filas.append(f"{_nombre:<20}{c:>9}{it:>9}{p:>9}{t:>12.4f}")
        self.tabla.delete("1.0", "end")
        self.tabla.insert("end", "\n".join(filas))


def main():
    if "--texto" in sys.argv:
        modo_texto()
        return
    root = tk.Tk()
    Comparativo(root)
    root.mainloop()


if __name__ == "__main__":
    main()