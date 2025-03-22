import random
import time

from bubblesort import bubblesort
from bubblesortotimiz import bubblesortotimiz

tamanhos = [100, 500, 1000, 5000]
resultados = []

def testar_algoritmo(algoritmo, lista):
    lista_copia = lista.copy() 
    inicio = time.time()
    iteracoes = algoritmo(lista_copia)
    tempo_execucao = time.time() - inicio
    return iteracoes, tempo_execucao

print("Comparação:")
print("")
for tamanho in tamanhos:
    lista_teste = []  
    for i in range(tamanho):  
        numero = random.randint(1, 10000)  
        lista_teste.append(numero)

    iteracoes_orig, tempo_orig = testar_algoritmo(bubblesort, lista_teste)
    iteracoes_otim, tempo_otim = testar_algoritmo(bubblesortotimiz, lista_teste)

    resultados.append((tamanho, iteracoes_orig, tempo_orig, iteracoes_otim, tempo_otim))

    print(f"Tamanho d lista: {tamanho}")
    print(f"Original: {iteracoes_orig} iterações, {tempo_orig:.6f} segundos")
    print(f"Otimizado: {iteracoes_otim} iterações, {tempo_otim:.6f}segundos")
    print("------------------------------------")
