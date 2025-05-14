import random

def ordenar(lista):
    if len(lista) < 2:
        return lista

    centro = len(lista) // 2
    lado_esquerdo = ordenar(lista[:centro])
    lado_direito = ordenar(lista[centro:])

    return intercalar(lado_esquerdo, lado_direito)

def intercalar(esq, dir):
    resultado = []
    i = j = 0

    while i < len(esq) and j < len(dir):
        if esq[i] <= dir[j]:
            resultado.append(esq[i])
            i += 1
        else:
            resultado.append(dir[j])
            j += 1

    resultado += esq[i:]
    resultado += dir[j:]

    return resultado

def testar_ordenacao():
    tamanhos = [1, 2, 40]
    
    for qtd in tamanhos:
        dados = random.sample(range(qtd * 5), qtd)
        ordenado = ordenar(dados)
        print(f"Lista com {qtd} elementos ordenada:")
        print(ordenado)
        print("-" * 40)

testar_ordenacao()
