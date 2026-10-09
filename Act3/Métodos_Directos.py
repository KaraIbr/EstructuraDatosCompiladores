def analisis_eficiencia():
    # Ejercicio 1: n = 20
    n1 = 20
    # Fórmula: C = (n^2 - n) / 2
    c_general = (n1**2 - n1) // 2 
    # Fórmula para selección: M = n - 1
    m_seleccion = n1 - 1
    
    print("--- Ejercicio 1 ---")
    print(f"Para n = {n1}:")
    print(f"Intercambio directo y Selección directa comparten C = {c_general} comparaciones.")
    print(f"Selección directa realiza M = {m_seleccion} movimientos.")
    
    # Ejercicio 2: n = 50 en un arreglo YA ordenado
    n2 = 50
    print("\n--- Ejercicio 2 ---")
    print(f"Para n = {n2} con arreglo ordenado:")
    
    # Inserción directa (mejor caso)
    c_insercion = n2 - 1
    m_insercion = 0
    total_insercion = c_insercion + m_insercion
    
    # Selección directa (comportamiento constante)
    c_seleccion = (n2**2 - n2) // 2
    m_seleccion2 = n2 - 1
    total_seleccion = c_seleccion + m_seleccion2
    
    print(f"Inserción Directa -> C: {c_insercion}, M: {m_insercion} | Total operaciones: {total_insercion}")
    print(f"Selección Directa -> C: {c_seleccion}, M: {m_seleccion2} | Total operaciones: {total_seleccion}")
    print("Conclusión: Inserción directa es superior (realiza menos operaciones) al evaluar arreglos ya ordenados.")

if __name__ == "__main__":
    analisis_eficiencia()