"""Visualizador animado de los cinco métodos de ordenación (Unidad 2).

Muestra barras animadas de cada algoritmo, con contadores en vivo,
notas de complejidad (mejor/peor) y el pseudocódigo en lenguaje
natural con la línea activa resaltada.

Uso:
    python visualizador.py
"""

import random
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

TIPOS_DATOS = ["aleatorio", "ordenado", "inverso", "casi_ordenado", "duplicados"]


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
    return base[:]


class Visualizador:
    def __init__(self, root):
        self.root = root
        root.title("Visualizador de métodos de ordenación - Unidad 2")
        root.configure(bg="#1e1e2e")

        self.n = 50
        self.velocidad = 20
        self.metodo = METODOS[0][1]
        self.datos = generar_datos("aleatorio", self.n)
        self.pasos = []
        self.idx = 0
        self.comparaciones = 0
        self.intercambios = 0
        self.pasadas = 0
        self.en_marcha = False

        self._crear_toolbar()
        self._crear_paneles()
        self._actualizar_pseudocodigo()
        self._actualizar_notas()
        self._dibujar(self.datos, "inicio", None, None)

    def _crear_toolbar(self):
        bar = ttk.Frame(self.root, padding=6)
        bar.pack(fill="x")

        ttk.Label(bar, text="Método:").pack(side="left")
        self.metodo_var = tk.StringVar(value=METODOS[0][0])
        for nombre, _mod in METODOS:
            ttk.Radiobutton(bar, text=nombre.split()[0], value=nombre,
                            variable=self.metodo_var,
                            command=self._cambiar_metodo).pack(side="left", padx=2)

        ttk.Label(bar, text="  Datos:").pack(side="left")
        self.tipo_var = tk.StringVar(value="aleatorio")
        for tipo in TIPOS_DATOS:
            ttk.Radiobutton(bar, text=tipo.replace("_", " "), value=tipo,
                            variable=self.tipo_var,
                            command=self._mejorar_actualizar).pack(side="left", padx=2)

        ttk.Label(bar, text="  Elementos:").pack(side="left")
        self.tam = ttk.Scale(bar, from_=10, to=90, value=self.n,
                             command=self._cambiar_tam)
        self.tam.pack(side="left", padx=2)

        ttk.Label(bar, text="  Velocidad:").pack(side="left")
        self.vel = ttk.Scale(bar, from_=5, to=120, value=self.velocidad,
                             command=self._cambiar_vel)
        self.vel.pack(side="left", padx=2)

        self.boton = ttk.Button(bar, text="▶ Ordenar", command=self._ordenar)
        self.boton.pack(side="left", padx=8)
        ttk.Button(bar, text="Mezclar", command=self._mejorar_actualizar).pack(side="left")

        self.estado = ttk.Label(bar, text="Listo", font=("Segoe UI", 9, "bold"))
        self.estado.pack(side="right")

    def _crear_paneles(self):
        cuerpo = ttk.Frame(self.root)
        cuerpo.pack(fill="both", expand=True)

        self.canvas = tk.Canvas(cuerpo, bg="#11111b", height=420)
        self.canvas.pack(side="left", fill="both", expand=True)

        lado = ttk.Frame(cuerpo, padding=8)
        lado.pack(side="right", fill="y")

        ttk.Label(lado, text="PSEUDOCÓDIGO", font=("Segoe UI", 10, "bold")).pack()
        self.pseudo = tk.Text(lado, width=46, height=12, state="disabled", wrap="word",
                              font=("Consolas", 9), bg="#1e1e2e", fg="#cdd6f4")
        self.pseudo.pack(pady=4)

        ttk.Label(lado, text="NOTAS (mejor/peor)", font=("Segoe UI", 10, "bold")).pack()
        self.notas = tk.Text(lado, width=46, height=7, state="disabled", wrap="word",
                             font=("Consolas", 9), bg="#1e1e2e", fg="#a6e3a1")
        self.notas.pack(pady=4)

        ttk.Label(lado, text="CONTADORES", font=("Segoe UI", 10, "bold")).pack()
        self.contadores = tk.Label(lado, text="comparaciones: 0   intercambios: 0   pasadas: 0",
                                   font=("Consolas", 10), bg="#11111b", fg="#f9e2af")
        self.contadores.pack(pady=4)

    # ---- acciones ----
    def _cambiar_metodo(self):
        nombre = self.metodo_var.get()
        self.metodo = next(m for nom, m in METODOS if nom == nombre)
        self._actualizar_pseudocodigo()
        self._actualizar_notas()

    def _cambiar_tam(self, _v):
        self.n = int(float(self.tam.get()))
        self._mejorar_actualizar()

    def _cambiar_vel(self, _v):
        self.velocidad = int(float(self.vel.get()))

    def _mejorar_actualizar(self):
        if self.en_marcha:
            return
        t = self.tipo_var.get()
        self.datos = generar_datos(t, self.n) if t != "duplicados" else \
            [random.randint(10, 80) for _ in range(self.n)]
        self._reset_contadores()
        self.estado.config(text="Listo")
        self._dibujar(self.datos, "inicio", None, None)

    def _ordenar(self):
        if self.en_marcha:
            return
        self.datos = [random.randint(10, 80) for _ in range(self.n)] \
            if self.tipo_var.get() == "duplicados" else self.datos
        self.pasos = list(self.metodo.pasos(self.datos))
        self.idx = 0
        self._reset_contadores()
        self.en_marcha = True
        self.boton.config(state="disabled")
        self.estado.config(text="Ordenando...")
        self._avanzar()

    def _avanzar(self):
        if self.idx >= len(self.pasos):
            self.en_marcha = False
            self.boton.config(state="normal")
            self.estado.config(text="Ordenado ✔")
            return
        arr, evento, i, j = self.pasos[self.idx]
        if evento == "comparar":
            self.comparaciones += 1
        elif evento in ("intercambiar", "desplazar"):
            self.intercambios += 1
        elif evento == "pasada":
            self.pasadas += 1
        self._dibujar(arr, evento, i, j)
        self._resaltar_pseudocodigo(evento)
        self.contadores.config(
            text=f"comparaciones: {self.comparaciones}   "
                 f"intercambios: {self.intercambios}   pasadas: {self.pasadas}")
        self.idx += 1
        delay = max(1, int(1000 / self.velocidad))
        self.root.after(delay, self._avanzar)

    def _reset_contadores(self):
        self.comparaciones = 0
        self.intercambios = 0
        self.pasadas = 0

    # ---- dibujo ----
    def _dibujar(self, arr, evento, i, j):
        c = self.canvas
        c.delete("all")
        n = len(arr)
        ancho, alto = c.winfo_width() or 800, c.winfo_height() or 380
        margen = 12
        maxv = max(arr, default=1)
        bar_w = max(2, (ancho - 2 * margen) / n)
        for k, v in enumerate(arr):
            h = v / maxv * (alto - 50)
            x0 = margen + k * bar_w
            color = "#89b4fa"
            if evento in ("comparar",) and k in (i, j):
                color = "#f38ba8"
            elif evento in ("intercambiar", "desplazar") and k in (i, j):
                color = "#a6e3a1"
            elif evento == "marcar" and k == i:
                color = "#f9e2af"
            c.create_rectangle(x0, alto - h, x0 + bar_w - 1, alto, fill=color, outline="")

    # ---- paneles de texto ----
    def _actualizar_pseudocodigo(self):
        self._llenar_texto(self.pseudo, self.metodo.PSEUDO)

    def _actualizar_notas(self):
        n = self.metodo.NOTAS
        lineas = [
            f"Mejor: {n['mejor']}", f"Peor: {n['peor']}",
            f"Promedio: {n['promedio']}", f"Memoria: {n['memoria']}",
            f"Estable: {n['estable']}", f"Adaptativo: {n['adaptativo']}",
        ]
        self._llenar_texto(self.notas, lineas)

    def _llenar_texto(self, widget, lineas):
        widget.config(state="normal")
        widget.delete("1.0", "end")
        for i, linea in enumerate(lineas, start=1):
            widget.insert("end", f"{i:>2}. {linea}\n")
        widget.config(state="disabled")

    def _resaltar_pseudocodigo(self, evento):
        widget = self.pseudo
        widget.tag_remove("resaltar", "1.0", "end")
        objetivo = None
        if evento in ("comparar",):
            objetivo = "compar"
        elif evento in ("intercambiar", "desplazar"):
            objetivo = "interca"
        elif evento == "marcar":
            objetivo = "menor"
        for i in range(1, int(widget.index("end-1c").split(".")[0]) + 1):
            if objetivo and objetivo.lower() in widget.get(f"{i}.0", f"{i}.end").lower():
                widget.tag_add("resaltar", f"{i}.0", f"{i}.end")
                break
        widget.tag_config("resaltar", background="#313244", foreground="#f9e2af",
                          font=("Consolas", 9, "bold"))


def main():
    root = tk.Tk()
    Visualizador(root)
    root.mainloop()


if __name__ == "__main__":
    main()