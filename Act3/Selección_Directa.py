def seleccion_directa(A, ejercicio=1):
    n = len(A)
    # El bucle va de 0 a n-2 (que es de 1 hasta N-1 en el algoritmo del libro)
    for i in range(n - 1):
        menor = A[i]
        k = i
        
        # Búsqueda del elemento menor en la parte no ordenada
        for j in range(i + 1, n):
            if A[j] < menor:
                menor = A[j]
                k = j
                
        if ejercicio == 1:
            print(f"Pasada {i+1}: Antes del intercambio -> MENOR: {menor}, K (índice): {k}")
            
        # Intercambio
        A[i], A[k] = A[k], A[i]
        
        if ejercicio == 1:
            print(f"           Arreglo resultante: {A}")
        elif ejercicio == 2:
            print(f"Pasada {i+1}: {A}")
            if i == 3:  # Termina después de 4 pasadas
                print("-> Se muestran solo las primeras cuatro pasadas")
                break
                
    return A

if __name__ == "__main__":
    print("--- Ejercicio 1: Arreglo [38, 14, 27, 09, 21, 33] ---")
    seleccion_directa([38, 14, 27, 9, 21, 33], ejercicio=1)
    
    print("\n--- Ejercicio 2: Arreglo [04, 18, 11, 29, 07, 25] ---")
    seleccion_directa([4, 18, 11, 29, 7, 25], ejercicio=2)