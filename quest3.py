#1 Não. Para listas pequenas, a alteração no cálculo do meio afeta de maneira sutil a forma como a divisão
#  acontece, mas, no geral, a lista será ordenada corretamente na maioria dos casos.

#2 Não. Modificar a forma de calcular o meio pode causar falhas no algoritmo, impedindo que o valor de meio
#  reduza corretamente o tamanho das sublistas, e resultando em chamadas recursivas com parâmetros repetidos.

#3 Sim, pode causar um erro ou levar a uma recursão infinita. Ao puxar o para a direita e realizar a chamada recursiva
#  merge_sorto meio pode acabar sendo igual ao fim, especialmente quando a lista possui poucos elementos. Isso faz com
#  que a sublista não diminuade tamanho, resultando em uma recursão infinita.

import random

def merge_sort_modificado(lista, ini, fim):
    if ini >= fim:
        return

    centro = (ini + fim) 
    merge_sort_modificado(lista, ini, centro)
    merge_sort_modificado(lista, centro + 1, fim)
    juntar(lista, ini, centro, fim)

def juntar(lista, ini, centro, fim):
    esquerda = lista[ini:centro + 1]
    direita = lista[centro + 1:fim + 1]

    i = j = 0
    k = ini

    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            lista[k] = esquerda[i]
            i += 1
        else:
            lista[k] = direita[j]
            j += 1
        k += 1

    while i < len(esquerda):
        lista[k] = esquerda[i]
        i += 1
        k += 1

    while j < len(direita):
        lista[k] = direita[j]
        j += 1
        k += 1

def testar():
    quantidades = [1, 2, 40]

    for qtd in quantidades:
        dados = random.sample(range(qtd * 10), qtd)
        merge_sort_modificado(dados, 0, len(dados) - 1)
        print(f"{qtd} elementos ordenados:")
        print(dados)
        print("-" * 40)

valores = [14, 13, 6, 7, 239, 11, 54]
merge_sort_modificado(valores, 0, len(valores) - 1)
print("Lista ordenada:", valores)

testar()