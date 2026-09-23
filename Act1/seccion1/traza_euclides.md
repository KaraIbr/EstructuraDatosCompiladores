# 1.1 traza de la pila de llamadas del algoritmo de euclides

llamada analizada: `mcd(21, 154)`.

definicion usada en el ejercicio 2.1:

    mcd(m, n) = mcd(n, m % n)   cuando n es mayor que cero
    mcd(m, 0) = m                cuando n es igual a cero

cada llamada recursiva crea un marco nuevo en la pila con sus propios
parametros. el marco mas reciente queda en la cima y no se puede devolver nada
hasta que la llamada que hizo regrese, por eso el resultado solo sube cuando
la ultima llamada encuentra el caso base.

## fase de descenso, marco por marco

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

que paso en cada marco, de arriba abajo:

```
marco 1  mcd(21, 154)
         n = 154 es mayor que cero, entonces no es caso base
         llamada generada: mcd(n, m % n) = mcd(154, 21 % 154) = mcd(154, 21)
         lo que queda pendiente en este marco: el valor que devuelva esa llamada

marco 2  mcd(154, 21)
         n = 21 es mayor que cero, entonces no es caso base
         llamada generada: mcd(21, 154 % 21) = mcd(21, 7)
         pendiente: el valor que devuelva mcd(21, 7)

marco 3  mcd(21, 7)
         n = 7 es mayor que cero, entonces no es caso base
         llamada generada: mcd(7, 21 % 7) = mcd(7, 0)
         pendiente: el valor que devuelva mcd(7, 0)

marco 4  mcd(7, 0)
         n = 0, se cumple el caso base
         devuelve 7
```

la forma de la pila en el instante de maxima profundidad es la del primer
dibujo: cuatro marcos simultaneos, el marco 4 arriba y el marco 1 abajo.

## fase de desapilamiento

ahora la pila se vacia de arriba abajo y cada marco recibe lo que devuelve la
llamada que habia lanzado.

```
marco 4  mcd(7, 0)    devuelve 7          la pila baja a 3 marcos
marco 3  mcd(21, 7)   recibe 7, devuelve 7    la pila baja a 2 marcos
marco 2  mcd(154, 21) recibe 7, devuelve 7    la pila baja a 1 marco
marco 1  mcd(21, 154) recibe 7, devuelve 7    la pila queda vacia
main     imprime  mcd = 7
```

el valor devuelto es el mismo en los cuatro marcos porque en esta version
simple no hay ninguna operacion pendiente: cada marco se limita a reenviar lo
que recibio. en el ejercicio 2.1 la funcion solo tiene el caso inductivo
`mcd(n, m % n)`, asi que el siete sube intacto desde el marco 4 hasta `main`.

## respuesta: cuantas llamadas se acumulan

en el punto de maxima profundidad hay 4 llamadas de pila simultaneas, o sea 4
marcos activos. como el algoritmo no genera ramas sino una sola cadena de
llamadas, el total de llamadas es tambien 4, una por cada division entera
necesaria: 154 % 21, 21 % 7, 7 % 0 y el retorno del caso base.

el residuo que baja a la segunda posicion de cada marco siempre es menor que
el valor que tenia antes, porque es un residuo modulo un numero mayor que
cero. por eso la recursion no puede repetirse y siempre se llega a `n = 0`.
el peor caso se da cuando ambos numeros son consecutivos, porque la primera
division casi no reduce el valor, y ahi la profundidad es del orden de
`log(n)`. para 21 y 154 la profundidad real es 4.
