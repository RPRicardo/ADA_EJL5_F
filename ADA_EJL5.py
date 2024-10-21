import heapq

def fusionar_listas(lists):
    # Crear un heap
    heap = []
    
    # Insertar el primer elemento de cada lista en el heap
    for i, lista in enumerate(lists):
        if lista:  # Si la lista no está vacía
            heapq.heappush(heap, (lista[0], i, 0))  # (valor, índice de la lista, índice del elemento en la lista)
    
    resultado = []
    
    # Extraer el menor elemento del heap y añadir el siguiente de la misma lista
    while heap:
        valor, lista_indice, elemento_indice = heapq.heappop(heap)
        resultado.append(valor)
        
        # Si hay más elementos en la misma lista, insertarlos en el heap
        if elemento_indice + 1 < len(lists[lista_indice]):
            siguiente_valor = lists[lista_indice][elemento_indice + 1]
            heapq.heappush(heap, (siguiente_valor, lista_indice, elemento_indice + 1))
    
    return resultado


# Ejecucion
lists1 = [[1,4,5], [1,3,4,6], [2,3,6,8]]
print(fusionar_listas(lists1))  


