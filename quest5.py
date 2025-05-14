import time
import random

def combinar(lista, inicio, meio, fim):
    esquerda = lista[inicio:meio + 1]
    direita = lista[meio + 1:fim + 1]

    i = j = 0
    atual = inicio

    while i < len(esquerda) and j < len(direita):
        if esquerda[i] <= direita[j]:
            lista[atual] = esquerda[i]
            i += 1
        else:
            lista[atual] = direita[j]
            j += 1
        atual += 1

    while i < len(esquerda):
        lista[atual] = esquerda[i]
        i += 1
        atual += 1

    while j < len(direita):
        lista[atual] = direita[j]
        j += 1
        atual += 1

def merge_sort_iterativo(lista):
    n = len(lista)
    passo = 1

    while passo < n:
        for inicio in range(0, n, 2 * passo):
            meio = min(inicio + passo - 1, n - 1)
            fim = min(inicio + 2 * passo - 1, n - 1)

            if meio < fim:
                combinar(lista, inicio, meio, fim)

        passo *= 2

def merge_sort_recursivo(lista):
    if len(lista) > 1:
        meio = len(lista) // 2
        parte_esq = lista[:meio]
        parte_dir = lista[meio:]

        merge_sort_recursivo(parte_esq)
        merge_sort_recursivo(parte_dir)

        i = j = k = 0

        while i < len(parte_esq) and j < len(parte_dir):
            if parte_esq[i] <= parte_dir[j]:
                lista[k] = parte_esq[i]
                i += 1
            else:
                lista[k] = parte_dir[j]
                j += 1
            k += 1

        while i < len(parte_esq):
            lista[k] = parte_esq[i]
            i += 1
            k += 1

        while j < len(parte_dir):
            lista[k] = parte_dir[j]
            j += 1
            k += 1

tamanhos = [100, 1000, 5000, 10000, 50000, 100000]
tempos = []

for tam in tamanhos:
    original = [random.randint(0, 10**6) for _ in range(tam)]

    lista1 = original.copy()
    inicio = time.perf_counter()
    merge_sort_recursivo(lista1)
    tempo_r = time.perf_counter() - inicio

    lista2 = original.copy()
    inicio = time.perf_counter()
    merge_sort_iterativo(lista2)
    tempo_i = time.perf_counter() - inicio

    tempos.append((tam, tempo_r, tempo_i))

for t in tempos:
    print(f"Tamanho: {t[0]}, Recursivo: {t[1]:.6f}s, Iterativo: {t[2]:.6f}s")
