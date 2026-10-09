def particion_quicksort(A, ini, fin, ejercicio=1, particion_num=1):
    izq = ini
    der = fin
    pos = ini
    band = True
    
    if ejercicio == 1:
        print(f"\n--- Partición inicial | Pivote: A[1] -> {A[pos]} ---")
        print(f"Estado original: {A}")
        
    while band:
        band = False
        # 1. Recorrido de derecha a izquierda
        while A[pos] <= A[der] and pos != der:
            der -= 1
        if pos != der:
            A[pos], A[der] = A[der], A[pos]
            pos = der
            if ejercicio == 1:
                print(f"Derecha->Izquierda (intercambio con el índice {der}): {A}")
            
            # 2. Recorrido de izquierda a derecha
            while A[pos] >= A[izq] and pos != izq:
                izq += 1
            if pos != izq:
                A[pos], A[izq] = A[izq], A[pos]
                pos = izq
                band = True
                if ejercicio == 1:
                    print(f"Izquierda->Derecha (intercambio con el índice {izq}): {A}")
                    
    if ejercicio == 2:
        sub_izq = A[ini:pos]
        sub_der = A[pos+1:fin+1]
        print(f"Partición {particion_num} completada | Pivote anclado: {A[pos]}")
        print(f"  -> Subconjuntos pendientes generados: Izquierdo {sub_izq} | Derecho {sub_der}")
        
    return pos

def quicksort_recursivo(A, ini, fin, ejercicio=2, estado=None):
    if estado is None:
        estado = {'num': 1}
        
    if ini < fin:
        if ejercicio == 1 and estado['num'] > 1:
            return  # El Ejercicio 1 solo demanda la primera partición
            
        pos = particion_quicksort(A, ini, fin, ejercicio, estado['num'])
        estado['num'] += 1
        
        quicksort_recursivo(A, ini, pos - 1, ejercicio, estado)
        quicksort_recursivo(A, pos + 1, fin, ejercicio, estado)
        
    return A

if __name__ == "__main__":
    print("--- Ejercicio 1: Solo primera partición ---")
    quicksort_recursivo([22, 41, 13, 35, 9, 28, 17], 0, 6, ejercicio=1)
    
    print("\n--- Ejercicio 2: Versión recursiva completa ---")
    quicksort_recursivo([34, 12, 27, 8, 19, 41, 15, 30], 0, 7, ejercicio=2)