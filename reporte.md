# actividad 2, metodos de ordenacion

reporte de la unidad 2 de la materia estructuras de datos y compiladores. el
codigo de esta actividad ya no usa datos primitivos exclusivamente, porque en
la unidad 2 si se trabajan los arreglos y por eso el objetivo ya no es la
recursividad sino la eficiencia con memoria auxiliar constante.

## que hay en la carpeta

- `ordenamientos/metodos` los cinco metodos de ordenacion directa, uno por
  archivo, cada uno con su pseudocodigo en la constante `pseudo` y su
  notacion de rendimiento en la constante `notas`.
- `ordenamientos/comparativo.py` corre los cinco metodos sobre los mismos
  datos y muestra comparaciones, intercambios, pasadas y tiempo real. con el
  argumento `--texto` imprime una tabla en la consola en vez de abrir la
  ventana grafica.
- `ordenamientos/visualizador.py` dibuja las barras animadas con tkinter,
  inspirado en el estilo de algebra visual.
- `ordenamientos/tests.py` la suite de pruebas con `unittest`.
- `ordenamientos/reflexion.md` la reflexion critica con los numeros medidos.
- `apunte-ordenamiento.md` las apuntes de clase que se usaron como referencia.

## notacion de rendimiento

burbuja: mejor o(n2), peor o(n2), memoria o(1), estable si, adaptativo no.

burbuja con senal: mejor o(n), peor o(n2), memoria o(1), estable si, adaptativo
si porque termina temprano si una pasada no intercambia.

sacudida: mejor o(n), peor o(n2), memoria o(1), estable si, adaptativo si
porque acorta el intervalo activo por los dos extremos.

insercion directa: mejor o(n), peor o(n2), memoria o(1), estable si, adaptativo
si porque no desplaza nada si el elemento ya esta en su lugar.

seleccion directa: mejor o(n2), peor o(n2), memoria o(1), estable no porque
puede saltarse el orden de dos elementos iguales, adaptativo no porque siempre
recorre el intervalo completo.

## resultados medidos

prueba con un arreglo aleatorio de 50 elementos promediando 10 corridas.

burbuja: 1225 comparaciones, 525 intercambios, 49 pasadas, 0.19 ms.

burbuja con senal: 1568 comparaciones, 525 intercambios, 32 pasadas, 0.27 ms.

sacudida: 792 comparaciones, 525 intercambios, 23 pasadas, 0.20 ms.

insercion directa: 574 comparaciones, 570 desplazamientos, 49 pasadas,
0.07 ms.

seleccion directa: 1225 comparaciones, 45 intercambios, 49 pasadas, 0.10 ms.

## conclusiones

los cinco metodos son o(n2) en el peor caso y todos usan o(1) de memoria
auxiliar, asi que solo son razonables con arreglos pequenos. el metodo mas
rapido en el caso aleatorio fue la insercion directa, porque compara poco
aunque mueve mucho. la seleccion directa es la que menos intercambios hace,
conviene cuando intercambiar es caro, pero no es estable. ni la senal ni la
sacudida mejoran el caso aleatorio, su ganancia aparece cuando los datos ya
estan casi ordenados. los cinco quedaron verificados con la suite de pruebas.

## como reproducir

```powershell
cd act2\ordenamientos
python -m unittest tests -v
python comparativo.py --texto
python visualizador.py
```
