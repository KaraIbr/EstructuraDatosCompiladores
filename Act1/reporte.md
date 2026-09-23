# practica 1: implementacion y analisis sistematico de soluciones recursivas

este archivo es el guion del informe en pdf. dice que va en cada pagina, en
que orden y que debe verse en cada una. el texto ya esta redactado, entonces
el trabajo que falta es pasarlo a word o a google docs, pegar las capturas de
la consola en los recuadros marcados como evidencia y exportar a pdf.

## pagina 1, caratula oficial

datos de la caratula, en este orden y centrados:

    global university
    estructuras de datos y compiladores
    practica 1. recursividad
    7.o cuatrimestre
    ingenieria en seguridad tecnologica y desarrollo de software
    asignatura fp34
    unidad 1, conceptos basicos y recursividad
    modalidad: individual
    alumno: nombre y matricula
    docente: nombre de la profesora
    ciudad y fecha de entrega

la caratula no lleva indice ni numeros de pagina.

## pagina 2, indice y resumen

indice con los titulos de primer nivel y el numero de pagina de cada uno:

```
1. caratula .................................................... 1
2. indice y resumen ............................................. 2
3. seccion 1. rastreo y seguimiento en memoria ................. 3
4. seccion 2. ejercicios de implementacion directa .............. 7
5. seccion 3. problemas de diseno y aplicacion ................. 10
6. resumen de los casos de prueba .............................. 13
7. evidencias de ejecucion ..................................... 14
8. conclusiones tecnicas ....................................... 18
9. checklist final y referencias ............................... 19
```

el resumen son tres parrafos: de que trata la practica, que se implementaron
once ejercicios con datos primitivos y recursividad, y que la conclusion
principal es que la pila de llamadas funciona como almacenamiento y que su
profundidad depende del problema.

## paginas 3 y 4, seccion 1.1 traza del algoritmo de euclides

pagina 3, la definicion y el descenso de la pila. se pega el contenido de
`Act1/seccion1/traza_euclides.md` hasta la tabla de los cuatro marcos, con el
dibujo de la pila en un marco de recuadro:

```
cima   ┌─────────────────────────────────────────────────────┐
       │ marco 1   m = 21    n = 154   (llamada inicial)     │
       ├─────────────────────────────────────────────────────┤
       │ marco 2   m = 154   n = 21    21 % 154 = 21         │
       ├─────────────────────────────────────────────────────┤
       │ marco 3   m = 21    n = 7     154 % 21 = 7          │
       ├─────────────────────────────────────────────────────┤
       │ marco 4   m = 7     n = 0     21 % 7 = 0            │
base   └─────────────────────────────────────────────────────┘
```

debajo del dibujo va la explicacion de cada marco: que valor tienen m y n, que
llamada genera y que queda pendiente. el orden de los residuo queda asi:

```
marco 1  mcd(21, 154)   genera  mcd(154, 21)     porque 21 % 154 = 21
marco 2  mcd(154, 21)   genera  mcd(21, 7)       porque 154 % 21 = 7
marco 3  mcd(21, 7)     genera  mcd(7, 0)        porque 21 % 7 = 0
marco 4  mcd(7, 0)      caso base, devuelve 7
```

pagina 4, la fase de desapilamiento y la respuesta a la pregunta del
enunciado:

```
marco 4  mcd(7, 0)    devuelve 7    la pila baja a 3 marcos
marco 3  mcd(21, 7)   recibe 7, devuelve 7    la pila baja a 2 marcos
marco 2  mcd(154, 21) recibe 7, devuelve 7    la pila baja a 1 marco
marco 1  mcd(21, 154) recibe 7, devuelve 7    la pila queda vacia
main     imprime  mcd = 7
```

la respuesta redactada es la siguiente: en el punto de maxima profundidad hay
4 llamadas de pila simultaneas, o sea 4 marcos activos. como el algoritmo no
genera ramas sino una sola cadena de llamadas, el total de llamadas tambien es
4, una por cada division entera necesaria. ademas el residuo que baja a la
segunda posicion de cada marco siempre es menor que el valor que tenia antes,
porque es un residuo modulo un numero mayor que cero, y por eso la recursion
no puede repetirse: siempre se llega a `n = 0`. el peor caso se da cuando los
dos numeros son consecutivos, y ahi la profundidad es del orden de `log(n)`.

## paginas 5 y 6, seccion 1.2 traza de la funcion de ackermann

pagina 5, la expansion paso a paso de `A(1, 2)` tal como esta en
`Act1/seccion1/traza_ackermann.md`, desde `A(1, 2)` hasta `A(0, 1)`, mas el
dibujo de los cuatro marcos simultaneos.

pagina 6, el orden exacto de resolucion de las llamadas internas:

```
1  A(0, 1)  devuelve 2      caso base, la primera que se resuelve
2  A(1, 0)  devuelve 2      reutiliza el 2 como segundo argumento
3  A(0, 2)  devuelve 3      se resuelve dentro de A(1, 1)
4  A(1, 1)  devuelve 3      reutiliza el 3 como segundo argumento
5  A(0, 3)  devuelve 4      se resuelve dentro de A(1, 2)
6  A(1, 2)  devuelve 4      ultimo marco en desapilar
```

son 6 llamadas en total y 4 marcos simultaneos. el resultado es 4, que
coincide con el caso de prueba 1 del ejercicio 2.2.

la respuesta a la pregunta del crecimiento exponencial, con estos datos
medidos anadiendo un contador de profundidad a la misma funcion:

```
A(1, 2) = 4    profundidad maxima = 4     llamadas totales = 6
A(2, 2) = 7    profundidad maxima = 8     llamadas totales = 27
A(3, 1) = 13   profundidad maxima = 15    llamadas totales = 106
A(3, 2) = 29   profundidad maxima = 31    llamadas totales = 541
A(3, 3) = 61   profundidad maxima = 63    llamadas totales = 2432
```

al subir `n` de 1 a 3 la profundidad pasa de 15 a 63, es decir
`2^(n + 4) - 1`, y el numero de llamadas casi se multiplica por cinco en cada
paso. la razon es que la rama `A(m - 1, A(m, n - 1))` obliga a terminar una
llamada completa antes de empezar la siguiente. ademas subir `m` de uno en uno
salta de nivel en la jerarquia: `A(1, n) = n + 2` y `A(2, n) = 2n + 3` son
lineales, `A(3, n) = 2^(n+3) - 3` ya es exponencial y `A(4, n)` es una torre
de exponenciales. la demostracion practica es que en python la version
directa ni siquiera alcanza: `A(4, 1)` deberia valer 65533 y la
implementacion aborta con `RecursionError` porque se queman los 1000 marcos
del limite por defecto.

## pagina 7, seccion 2.1 maximo comun divisor

la definicion del enunciado, la teoria y el codigo, en este orden:

caso base, redactado: ocurre cuando el segundo parametro n es igual a cero. en
ese momento el primer parametro ya es multiplo del segundo, no queda nada que
dividir y la funcion se detiene devolviendo m.

caso inductivo, redactado: ocurre cuando n es mayor que cero. la funcion se
invoca a si misma pasando n como primer argumento y el residuo de `m % n` como
segundo argumento. el segundo operando siempre baja, porque un residuo es
menor que el divisor, y por eso la cadena de llamadas siempre llega al caso
base en un numero finito de pasos.

```
def mcd(m, n):
    """devuelve el maximo comun divisor de m y n.

    caso base: si n vale cero, el dividendo ya es multiplo del otro numero
    y se devuelve directamente.
    caso inductivo: si n es mayor que cero, el mismo problema se resuelve
    con el residuo de dividir m entre n, pasando n como nuevo primer
    operando para que el segundo operando siempre baje.
    """
    if n == 0:  # caso base
        return m
    # caso inductivo
    return mcd(n, m % n)
```

## pagina 8, seccion 2.2 funcion de ackermann

caso base, redactado: ocurre cuando m vale cero. es el unico punto donde la
recursion se detiene y la funcion devuelve `n + 1`.

caso inductivo, redactado: si m es mayor que cero y n vale cero, se reduce m
en uno y se reinicia n en uno. si m y n son mayores que cero, primero se
resuelve la llamada interna `A(m, n - 1)` y su resultado se usa como segundo
argumento de `A(m - 1, ...)`. esa llamada interna es la que hace crecer la
pila, porque debe completarse antes de que la externa pueda ejecutarse.

```
def ackermann(m, n):
    """devuelve el valor de A(m, n).

    caso base: si m vale cero, la funcion se detiene y devuelve n + 1.
    caso inductivo: si m es mayor que cero y n vale cero, se reduce m en uno
    y se reinicia n en uno. si los dos son mayores que cero, primero se
    resuelve A(m, n - 1) y ese resultado se usa como segundo argumento de
    A(m - 1, ...).
    """
    if m == 0:  # caso base: unico punto donde la recursion se detiene
        return n + 1
    if n == 0:  # caso inductivo: se baja m en uno y se reinicia n en uno
        return ackermann(m - 1, 1)
    # caso inductivo: la llamada interna se resuelve antes de la externa
    interno = ackermann(m, n - 1)
    return ackermann(m - 1, interno)
```

## pagina 9, seccion 2.3 particiones de un entero

caso base, redactado: se alcanza cuando m vale 1 o cuando n vale 1, porque en
los dos casos hay una unica forma posible, y se devuelve 1.

caso inductivo, redactado: si m es menor que n, el limite superior se ajusta
a m porque no tiene sentido usar un numero mayor que el total. si m es igual
que n, se cuenta la forma directa que usa solo m y se suman las que no lo usan.
si m es mayor que n, se suman las particiones que no incluyen a n,
`P(m, n - 1)`, con las que incluyen al menos un termino n, `P(m - n, n)`. en
los tres casos los dos parametros bajan, asi que la recursion termina.

```
def particiones(m, n):
    """devuelve cuantas formas hay de escribir m como suma de 1 hasta n.

    caso base: si m vale 1 o si n vale 1 hay una unica forma, se devuelve 1.
    caso inductivo: si m es menor que n el limite superior se ajusta a m; si
    m es igual que n se cuenta la forma que usa solo m y se suman las que no
    lo usan; si m es mayor que n se suman las particiones que no usan n con
    las que usan al menos un n.
    """
    if m == 1 or n == 1:  # caso base
        return 1
    if m < n:  # caso inductivo
        return particiones(m, m)
    if m == n:  # caso inductivo
        return 1 + particiones(m, m - 1)
    # caso inductivo
    return particiones(m, n - 1) + particiones(m - n, n)
```

## pagina 10, seccion 3.1 y 3.2

ejercicio 3.1 multiplicacion mediante sumas. caso base: si n vale cero, el
producto es cero porque es el neutro de la suma, y no queda nada por sumar.
caso inductivo: si n es mayor que cero, el producto es m mas el producto de m
por n - 1, con lo cual la segunda cantidad baja de uno en uno.

```
def multiplicar(m, n):
    if n == 0:  # caso base
        return 0
    # caso inductivo
    return m + multiplicar(m, n - 1)
```

ejercicio 3.2 potencia entera. caso base: si n vale cero, cualquier numero
elevado a cero da uno, que es el neutro de la multiplicacion. caso inductivo:
si n es mayor que cero, el resultado es a multiplicado por a elevado a n - 1,
de modo que el exponente baja de uno en uno.

```
def potencia(a, n):
    if n == 0:  # caso base
        return 1
    # caso inductivo
    return a * potencia(a, n - 1)
```

## pagina 11, seccion 3.3, 3.4 y 3.5

ejercicio 3.3 serie armonica. caso base: si n vale cero o es negativo, no
queda termino por sumar y la suma acumulada es cero. caso inductivo: si n es
mayor que cero, la suma es `1 / n` mas la suma de los primeros n - 1 terminos.

```
def serie_armonica(n):
    if n <= 0:  # caso base
        return 0.0
    # caso inductivo
    return 1 / n + serie_armonica(n - 1)
```

ejercicio 3.4 impresion de impares. caso base: si n es menor o igual que cero
la funcion finaliza sin imprimir. caso inductivo: si n es mayor que cero, la
llamada con n - 1 se resuelve primero y al volver se imprime n cuando es
impar. el orden importa, porque imprimir antes de la llamada daria la
secuencia al reves.

```
def imprimir_impares(n):
    if n <= 0:  # caso base
        return
    # caso inductivo
    imprimir_impares(n - 1)
    if n % 2 != 0:
        print(n, end=" ")
```

ejercicio 3.5 inversion por la pila. caso base: si el entero leido es cero, no
se hace ninguna llamada mas y empieza el desapilamiento. caso inductivo: si
es distinto de cero, primero se resuelve la llamada interna, que lee el
siguiente dato, y solo despues se imprime el valor que quedo guardado en ese
marco de pila. no hay ningun arreglo: el valor se conserva en la variable
local x del marco mientras la pila crece.

```
def invertir():
    x = int(input("ingrese un entero positivo, cero termina: "))
    if x == 0:  # caso base
        return
    # caso inductivo
    invertir()
    print(x, end=" ")
```

## pagina 12, seccion 3.6, 3.7 y 3.8

ejercicio 3.6 conteo de cifras. caso base: si n es menor que diez, el numero
tiene un solo digito y se devuelve uno. caso inductivo: si n es mayor o igual
que diez, se cuenta el digito de las unidades y se suman las cifras de
`n // 10`, que es un numero mas corto.

```
def contar_digitos(n):
    if n < 10:  # caso base
        return 1
    # caso inductivo
    return 1 + contar_digitos(n // 10)
```

ejercicio 3.7 digitos invertidos. caso base: si n es menor que diez, se imprime
el digito directamente. caso inductivo: si n es mayor o igual que diez, se
imprime primero el residuo de la division entre diez, que es el digito de la
derecha, y despues se resuelve la llamada con la parte entera.

```
def imprimir_digitos_inversos(n):
    if n < 10:  # caso base
        print(n, end="")
        return
    # caso inductivo
    print(n % 10, end="")
    imprimir_digitos_inversos(n // 10)
```

ejercicio 3.8 digitos separados por espacio. caso base: si n es menor que diez,
se imprime el digito seguido de un espacio. caso inductivo: si n es mayor o
igual que diez, primero se resuelve la llamada con la parte entera, que deja
impresos los digitos de la izquierda, y al volver se imprime el digito de las
unidades, que es el ultimo.

```
def imprimir_digitos_espaciados(n):
    if n < 10:  # caso base
        print(n, end=" ")
        return
    # caso inductivo
    imprimir_digitos_espaciados(n // 10)
    print(n % 10, end=" ")
```

## pagina 13, resumen de los casos de prueba

esta tabla demuestra que los 22 casos obligatorios se ejecutaron. la columna
de salida obtenida se lleno con lo que realmente mostro la consola.

```
ejercicio  entrada          salida esperada        salida obtenida
2.1        21  154          mcd = 7                mcd = 7
2.1        231  182         mcd = 7                mcd = 7
2.2        1  2             resultado = 4          resultado = 4
2.2        2  2             resultado = 7          resultado = 7
2.3        5  5             total = 7              total de particiones = 7
2.3        6  6             total = 11             total de particiones = 11
3.1        8  3             producto = 24          producto = 24
3.1        12  5            producto = 60          producto = 60
3.2        2  3             potencia = 8           potencia = 8
3.2        5  4             potencia = 625         potencia = 625
3.3        1                suma = 1.0             suma = 1.00000
3.3        4                suma = 2.08333         suma = 2.08333
3.4        10               1 3 5 7 9              1 3 5 7 9
3.4        15               1 3 5 7 9 11 13 15     1 3 5 7 9 11 13 15
3.5        4 9 2 0          2 9 4                  2 9 4
3.5        15 23 8 42 1 0   1 42 8 23 15          1 42 8 23 15
3.6        7654             cifras = 4             cifras = 4
3.6        9                cifras = 1             cifras = 1
3.7        4567             7654                   7654
3.7        1200             0021                   0021
3.8        4567             4 5 6 7                4 5 6 7
3.8        80921            8 0 9 2 1              8 0 9 2 1
```

la suite automatizada ejecuta 17 pruebas con `python -m unittest pruebas -v`,
que cubren los 14 casos de prueba que devuelven un valor. los 8 casos
restantes son los de los ejercicios 3.4, 3.5, 3.7 y 3.8, que solo imprimen, y
se demuestran con las capturas de las paginas 14 a 17.

## paginas 14 a 17, evidencias de ejecucion

en cada pagina van tres recuadros con la captura de la consola. la leyenda va
debajo de cada recuadro y dice: ejercicio, caso de prueba, entrada, salida
esperada, y que coincide.

```
+-------------------------------------------------------------+
| evidencia: ejercicio 2.1, caso de prueba 1                   |
| entrada 21 154, salida esperada mcd = 7, coincide           |
| [ aqui va la captura de pantalla de la consola ]             |
+-------------------------------------------------------------+

+-------------------------------------------------------------+
| evidencia: ejercicio 2.1, caso de prueba 2                   |
| entrada 231 182, salida esperada mcd = 7, coincide          |
| [ aqui va la captura de pantalla de la consola ]             |
+-------------------------------------------------------------+
```

la distribucion sugerida es: pagina 14 con los ejercicios 2.1, 2.2 y 2.3;
pagina 15 con 3.1, 3.2 y 3.3; pagina 16 con 3.4, 3.5 y 3.6; pagina 17 con 3.7
y 3.8. en cada captura se deben ver el titulo del ejercicio, la pregunta que
hace el programa, el dato que se escribio y la linea de resultado.

## pagina 18, conclusiones tecnicas

conclusion 1: la recursion es una forma de reemplazar los ciclos por la pila
de llamadas. cada llamada guarda sus variables locales en un marco y la
pila hace las veces de almacenamiento, como se ve en el ejercicio 3.5, donde
la sucesion se invierte sin un solo arreglo.

conclusion 2: la profundidad de la pila no depende de la cantidad de datos
sino de como se reduce el problema. el mcd de 21 y 154 necesita cuatro marcos
porque cada division reduce el segundo operando, mientras que la serie
armonica necesita tantos marcos como terminos.

conclusion 3: ackermann muestra el limite. un incremento de m sube de nivel
en la jerarquia de funciones iteradas y a partir de `A(3, n)` el numero de
llamadas crece de forma exponencial, hasta el punto de que la version
recursiva directa desborda la pila antes de terminar.

conclusion 4: el orden de las llamadas dentro de una funcion recursiva cambia
el resultado. imprimir antes de la llamada recursiva da la secuencia al reves,
y el orden inverso la da en orden ascendente. el mismo razonamiento aplica a
las particiones, donde sumar en el orden equivocado cuenta combinaciones de
mas.

## pagina 19, checklist final y referencias

el checklist se imprime en la pagina y se marca con una palomita a mano.

```
[ ] ningun archivo de Act1 usa listas, tuplas, diccionarios, conjuntos ni
    arreglos: cero corchetes y cero llamadas a list, tuple, dict o set
[ ] ningun archivo de Act1 usa ciclos for ni while, la unica forma de
    repetir es la llamada recursiva
[ ] los once archivos de los ejercicios no importan nada de la biblioteca
    estandar
[ ] cada funcion recursiva trae en su encabezado el comentario del caso base
    y el del caso inductivo
[ ] los 22 casos de prueba obligatorios se ejecutaron y coinciden
[ ] el informe incluye los dos diagramas de la pila de llamadas
[ ] el informe incluye las 11 capturas de evidencia de las paginas 14 a 17
[ ] el codigo va indentado con cuatro espacios y con el docstring arriba
[ ] el pdf y el zip se llaman Practica1_Recursividad_FP34
[ ] el zip no se sube al repositorio, solo a google classroom
```

comando que respalda el checklist de datos primitivos:

```powershell
Select-String -Path .\Act1\seccion2\*.py, .\Act1\seccion3\*.py -Pattern "\[|\blist\(|\btuple\(|\dict\(|\bset\(|\bfor |\bwhile |^import |^from "
```

la ordenacion de arriba tiene que devolver cero resultados.

para armar el entregable:

```powershell
cd <carpeta-del-repositorio>
New-Item -ItemType Directory -Force -Path .\entrega\fuente | Out-Null
Copy-Item .\Act1\seccion2\*.py, .\Act1\seccion3\*.py, .\Act1\pruebas.py -Destination .\entrega\fuente
Copy-Item .\Practica1_Recursividad_FP34.pdf -Destination .\entrega
Compress-Archive -Path .\entrega\* -DestinationPath .\Practica1_Recursividad_FP34.zip -Force
```

el zip debe contener el pdf del informe y la carpeta `fuente` con los once
programas mas el archivo de pruebas. referencias: apuntes de la unidad 1
compartidos en clase, material de cairo capitulo 8 para notacion de
ordenamientos, y documentacion oficial de python 3.10 en docs.python.org.
