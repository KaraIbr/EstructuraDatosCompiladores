# estructuras de datos y compiladores

repositorio de la asignatura fp34 del septimo cuatrimestre de ingenieria en
seguridad tecnologica y desarrollo de software de global university.

cada practica vive en su propia carpeta, con el codigo ejecutable, las pruebas
y el reporte de la unidad, para que la evolucion del curso se pueda leer en
orden.

## contenido

- `act1` practica 1, recursividad. once ejercicios con solo datos primitivos,
  dos trazas de la pila de llamadas y el reporte de la practica.
- `act2` unidad 2, ordenamientos. los cinco metodos de ordenacion directa con
  su notacion de rendimiento, el visualizador grafico, la prueba comparativa y
  las apuntes de clase.

## como ejecutar

```powershell
cd act1
python seccion2\ej2_1_mcd.py
python seccion3\ej3_5_inversion.py
python -m unittest pruebas -v
```

```powershell
cd act2\ordenamientos
python comparativo.py --texto
python -m unittest tests -v
```

cada archivo de `act1` se ejecuta por separado y pide sus datos por consola,
de modo que la evidencia de cada caso de prueba se puede capturar en pantalla.

## requisitos

solo python 3.10 o superior con la libreria estandar, nada mas se instala.

el visualizador de `act2` ademas usa tkinter, que viene con la instalacion
normal de python en windows.

## notas de estilo

las practicas de `act1` excluyen arreglos, listas, tuplas y diccionarios a
proposito, porque todavia no se ven estructuras de datos compuestas. la
recursividad y la pila de llamadas son el unico mecanismo de control de flujo
y de almacenamiento, asi que no hay ciclos `for` ni `while` en el codigo de
los ejercicios.

## licencia

codigo publicado bajo la licencia mit que aparece en el archivo `license`.
