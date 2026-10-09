def burbuja_senal(A, ejercicio=1):
    n = len(A)
    i = 0
    band = False
    
    # Se ejecuta mientras no se alcance el final y hayan ocurrido intercambios
    while i < n - 1 and not band:
        band_al_inicio = True  # Suponemos que ya está ordenado
        band = True 
        ultimo_intercambio = -1
        
        for j in range(0, n - 1 - i):
            if A[j] > A[j + 1]:
                # Intercambio
                A[j], A[j + 1] = A[j + 1], A[j]
                band = False  # Hubo un intercambio, el arreglo aún no está ordenado
                ultimo_intercambio = j
                
        i += 1
        
        # Impresión específica para el Ejercicio 2 en su primera pasada
        if ejercicio == 2 and i == 1:
            print(f"-> Registro BAND pasada 1 | Inicio: {band_al_inicio} | Final: {band}")
            
        if not band:
            print(f"Pasada {i}: {A} | Último intercambio en índice {ultimo_intercambio}")
        else:
            print(f"Pasada {i}: {A} | BAND se mantuvo {band} (Sin intercambios). Proceso terminado.")
            
    return A

if __name__ == "__main__":
    print("--- Ejercicio 1: Arreglo [08, 12, 15, 27, 16, 35, 44] ---")
    burbuja_senal([8, 12, 15, 27, 16, 35, 44], ejercicio=1)
    
    print("\n--- Ejercicio 2: Arreglo [05, 10, 15, 20, 25] ---")
    burbuja_senal([5, 10, 15, 20, 25], ejercicio=2)