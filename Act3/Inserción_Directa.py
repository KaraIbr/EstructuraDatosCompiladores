def insercion_directa(A, objetivo_seguimiento=None):
    n = len(A)
    for i in range(1, n):
        aux = A[i]
        k = i - 1
        
        comparaciones = 0
        desplazamientos = 0
        
        # Desplaza los elementos mayores a la derecha
        while k >= 0 and aux < A[k]:
            A[k + 1] = A[k]
            k -= 1
            comparaciones += 1
            desplazamientos += 1
            
        # Si el ciclo while termina por k < 0 o aux >= A[k], suma esa última comparación
        if k >= 0:
            comparaciones += 1
            
        A[k + 1] = aux
        
        # Impresión de estado general
        print(f"Pasada {i}: Parte ordenada izquierda -> {A[:i+1]}")
        
        # Seguimiento específico para el ejercicio 2
        if aux == objetivo_seguimiento:
            print(f"  -> Al insertar {aux}: {comparaciones} comparaciones, {desplazamientos} desplazamientos.")
            
    return A

if __name__ == "__main__":
    print("--- Inserción Directa (Ejercicio 1) ---")
    insercion_directa([24, 13, 18, 9, 31, 16])
    
    print("\n--- Inserción Directa (Ejercicio 2 - Seguir el 20) ---")
    insercion_directa([7, 12, 18, 25, 20, 30], objetivo_seguimiento=20)