def shell_sort(A, ejercicio=1):
    n = len(A)
    # Inicialización del intervalo INT
    intervalo = (n + 1) // 2
    
    while intervalo > 0:
        if ejercicio == 2:
            # Identificación y agrupamiento de los subconjuntos lógicos
            grupos = []
            for i in range(intervalo):
                grupo = [A[j] for j in range(i, n, intervalo)]
                grupos.append(grupo)
            print(f"\nIntervalo INT = {intervalo}")
            for i, g in enumerate(grupos):
                print(f"  Grupo {i+1}: {g}")
                
        # Proceso de comparaciones tipo burbuja a través de los incrementos
        band = True
        while band:
            band = False
            i = 0
            while (i + intervalo) < n:
                if A[i] > A[i + intervalo]:
                    A[i], A[i + intervalo] = A[i + intervalo], A[i]
                    band = True
                i += 1
                
        if ejercicio == 1:
            print(f"Arreglo finalizada la pasada con INT={intervalo}: {A}")
            
        if intervalo == 1:
            break
        # Reducción a la mitad entera
        intervalo = intervalo // 2
        
    return A

if __name__ == "__main__":
    print("--- Ejercicio 1: Arreglo de 8 elementos ---")
    shell_sort([32, 14, 27, 9, 45, 18, 21, 6], ejercicio=1)
    
    print("\n--- Ejercicio 2: Grupos en arreglo de 16 elementos ---")
    shell_sort([40, 12, 35, 8, 27, 19, 31, 5, 44, 16, 23, 10, 38, 21, 29, 7], ejercicio=2)