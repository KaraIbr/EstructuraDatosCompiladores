# Reflexión crítica — Métodos de ordenación (Unidad 2)

## Resultado experimental
Los cinco métodos se corrieron sobre el mismo arreglo aleatorio de
50 elementos (promedio de 10 corridas):

| Método | Comparaciones | Intercambios | Pasadas | Tiempo (ms) |
|---|---|---|---|---|
| Burbuja | 1225 | 525 | 49 | 0.19 |
| Burbuja con señal | 1568 | 525 | 32 | 0.27 |
| Sacudida | 792 | 525 | 23 | 0.20 |
| Inserción directa | 574 | 570 | 49 | 0.07 |
| Selección directa | 1225 | 45 | 49 | 0.10 |

## Análisis
- **Burbuja con señal** hace más comparaciones que la burbuja simple
  en datos aleatorios (1568 > 1225): la bandera solo ayuda cuando el
  arreglo está casi ordenado, no en un caso aleatorio promedio.
- **Sacudida** reduce comparaciones casi a la mitad (792) porque acorta
  el intervalo por ambos extremos; es la mejor de la familia burbuja.
- **Inserción directa** fue la más rápida: hace pocas comparaciones
  (574) aunque muchos movimientos (570); brilla con datos casi ordenados.
- **Selección directa** siempre compara n(n-1)/2 (1225) sin importar los
  datos, pero hace el menor número de intercambios (45): conviene cuando
  el intercambio es costoso. No es estable.
- Los demás son estables y adaptativos; todos son O(n^2), por lo que solo
  sirven con arreglos pequeños (lo común en la vida real es usar un
  método avanzado como Quick/Merge, que se ve en la siguiente unidad).

## Conclusión
Los cinco cumplen con su definición teórica (Cairo, cap. 8) y quedaron
verificados con las pruebas automáticas (`python -m unittest tests -v`).
La práctica permitió ver que la eficiencia "mejor caso" depende del
orden inicial de los datos y que optimizaciones como la señal o la
sacudida no siempre mejoran el caso aleatorio, sino el caso casi ordenado.