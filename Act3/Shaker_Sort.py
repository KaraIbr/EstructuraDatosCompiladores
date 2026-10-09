def shaker_sort(A, ejercicio=1):
    n = len(A)
    izq = 1
    der = n - 1
    k = n - 1
    etapa = 1
    
    while der >= izq:
        intercambio_realizado = False
        
        # Etapa 1: Derecha a Izquierda (mueve los menores al principio)
        for i in range(der, izq - 1, -1):
            if A[i - 1] > A[i]:
                # Intercambio
                A[i - 1], A[i] = A[i], A[i - 1]
                k = i
                intercambio_realizado = True
                
        # Se actualiza el límite izquierdo
        izq = k + 1
        print(f"Pasada {etapa} (Der->Izq): {A} | Último intercambio en: {k} | Límites: IZQ={izq}, DER={der}")
        
        # Etapa 2: Izquierda a Derecha (mueve los mayores al final)
        for i in range(izq, der + 1):
            if A[i - 1] > A[i]:
                # Intercambio
                A[i - 1], A[i] = A[i], A[i - 1]
                k = i
                intercambio_realizado = True
                
        # Se actualiza el límite derecho
        der = k - 1
        print(f"Pasada {etapa} (Izq->Der): {A} | Último intercambio en: {k} | Límites: IZQ={izq}, DER={der}")
        
        # Criterio de paro por ausencia de intercambios
        if not intercambio_realizado:
            if ejercicio == 2:
                print("-> CONCLUSIÓN: Al no registrarse ningún intercambio en la etapa, se confirma "
                      "que el arreglo ya está ordenado. Esto rompe el ciclo y concluye el proceso anticipadamente.")
            else:
                print("-> Sin intercambios. Proceso terminado.")
            break
            
        etapa += 1
        
    return A

if __name__ == "__main__":
    print("--- Ejercicio 1: Arreglo [29, 11, 42, 08, 35, 17, 24] ---")
    shaker_sort([29, 11, 42, 8, 35, 17, 24], ejercicio=1)
    
    print("\n--- Ejercicio 2: Arreglo [05, 07, 09, 12, 11, 15, 18] ---")
    shaker_sort([5, 7, 9, 12, 11, 15, 18], ejercicio=2)