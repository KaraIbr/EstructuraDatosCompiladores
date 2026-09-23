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
