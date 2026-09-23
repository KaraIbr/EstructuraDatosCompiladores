# 1.2 traza de la pila de llamadas de la funcion de ackermann

llamada analizada: `A(1, 2)`.

definicion usada en el ejercicio 2.2:

    A(0, n) = n + 1                    cuando m vale cero
    A(m, 0) = A(m - 1, 1)              cuando m es mayor que cero y n vale cero
    A(m, n) = A(m - 1, A(m, n - 1))    cuando m es mayor que cero y n es mayor que cero

esta definicion se comporta distinto a la de euclides porque la tercera rama
tiene una llamada anidada dentro de otra. el lenguaje resuelve primero los
argumentos de una llamada, o sea que `A(m, n - 1)` se completa por completo
antes de que se pueda invocar `A(m - 1, ...)`. por eso las llamadas internas
se resuelven de adentro hacia afuera.

## expansion paso a paso

```
A(1, 2)
  se necesita el segundo argumento de la llamada externa: A(1, 1)

    A(1, 1)
      se necesita el segundo argumento de esta llamada: A(1, 0)

        A(1, 0)
          n vale cero, entra en la segunda rama
          se llama A(m - 1, 1) = A(0, 1)

            A(0, 1)
              m vale cero, caso base
              devuelve 1 + 1 = 2

        A(1, 0) recibe 2 y devuelve 2

      A(1, 1) ya tiene su segundo argumento, llama A(0, 2)

        A(0, 2)
          m vale cero, caso base
          devuelve 2 + 1 = 3

    A(1, 1) devuelve 3

A(1, 2) ya tiene su segundo argumento, llama A(0, 3)

  A(0, 3)
    m vale cero, caso base
    devuelve 3 + 1 = 4

A(1, 2) devuelve 4
```

## forma de la pila en el punto de maxima profundidad

```
cima   ┌──────────────────────────────────────────────┐
       │ A(0, 1)   espera el resultado, ya esta en    │
       │            el caso base y va a devolver 2    │
       ├──────────────────────────────────────────────┤
       │ A(1, 0)   espera a A(0, 1) para poder        │
       │            llamar a A(0, 2)                   │
       ├──────────────────────────────────────────────┤
       │ A(1, 1)   espera a A(1, 0) para poder llamar  │
       │            a A(0, 3)                          │
       ├──────────────────────────────────────────────┤
       │ A(1, 2)   espera a A(1, 1) para poder llamar  │
       │            a A(0, 4)                          │
base   └──────────────────────────────────────────────┘
```

## orden exacto de resolucion

las llamadas se resuelven asi, de la mas interna a la mas externa:

```
1  A(0, 1)  devuelve 2      caso base, la primera que se resuelve
2  A(1, 0)  devuelve 2      reutiliza el 2 como segundo argumento
3  A(0, 2)  devuelve 3      se resuelve dentro de A(1, 1)
4  A(1, 1)  devuelve 3      reutiliza el 3 como segundo argumento
5  A(0, 3)  devuelve 4      se resuelve dentro de A(1, 2)
6  A(1, 2)  devuelve 4      ultimo marco en desapilar
```

son 6 llamadas en total y 4 marcos simultaneos en el punto de maxima
profundidad. el resultado esperado es 4, que coincide con el caso de prueba 1
del ejercicio 2.2.

## respuesta: por que un incremento pequeno desata un crecimiento exponencial

la razon es que la tercera rama `A(m - 1, A(m, n - 1))` obliga a terminar una
llamada completa antes de empezar la siguiente, de modo que la profundidad no
crece de forma lineal con los parametros.

medido con un contador de profundidad sobre la misma funcion:

```
A(1, 2) = 4    profundidad maxima = 4     llamadas totales = 6
A(2, 2) = 7    profundidad maxima = 8     llamadas totales = 27
A(3, 1) = 13   profundidad maxima = 15    llamadas totales = 106
A(3, 2) = 29   profundidad maxima = 31    llamadas totales = 541
A(3, 3) = 61   profundidad maxima = 63    llamadas totales = 2432
```

al subir `n` de 1 a 3 la profundidad pasa de 15 a 63, o sea `2^(n + 4) - 1`, y
el numero de llamadas casi se multiplica por cinco en cada paso. con solo tres
unidades de diferencia la pila ya se cuadruplica.

ademas, subir `m` de uno en uno salta de nivel en la jerarquia de funciones
iteradas:

```
A(1, n) = n + 2        lineal
A(2, n) = 2n + 3       lineal
A(3, n) = 2^(n+3) - 3  exponencial
A(4, n)                torre de exponenciales
```

la consecuencia practica es que la version directa de la definicion no
alcanza: en python, `A(4, 1)` deberia valer 65533 y sin embargo la
implementacion aborta con `RecursionError` porque el limite de 1000 marcos se
quema antes de terminar el calculo. eso es la demostracion empirica de que el
crecimiento de la profundidad es exponencial y no lineal.
