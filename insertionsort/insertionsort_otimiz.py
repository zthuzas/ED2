from insertionsort import insertionsort
import time 
import copy

def insertionsort_otimizado(array):
    movimentacoes = 0
    n = len(array)
    for i in range(1, n):
        chave = array[i]
        j = i - 1
        trocou = False
        while j >= 0 and array[j] > chave:
            array[j + 1] = array[j]
            j -= 1
            movimentacoes += 1
            trocou = True
        array[j + 1] = chave
        if not trocou:
            break 
    return movimentacoes


tamanho = 1000
vetor_ordenado = list(range(tamanho))
    
vetor1 = copy.deepcopy(vetor_ordenado)
vetor2 = copy.deepcopy(vetor_ordenado)

print("Vetor já ordenado, tamanho =", tamanho)

inicio = time.time()
mov1 = insertionsort(vetor1)
tempo1 = time.time() - inicio

inicio = time.time()
mov2 = insertionsort_otimizado(vetor2)
tempo2 = time.time() - inicio

print("Insertion Sort:")
print("Movimentações: {mov1}")
print("Tempo: {tempo1:.6f}s")

print("Insertion Sort Otimiz:")
print("Movimentações: {mov2}")
print("Tempo: {tempo2:.6f} segundos")


