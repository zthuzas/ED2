def ordenar_merge(lista):
    if len(lista) < 2:
        return lista

    ponto_medio = len(lista) // 2
    esquerda = ordenar_merge(lista[:ponto_medio])
    direita = ordenar_merge(lista[ponto_medio:])

    return combinar(esquerda, direita)

def combinar(esq, dir):
    combinado = []
    i, j = 0, 0

    while i < len(esq) and j < len(dir):
        if esq[i] >= dir[j]:
            combinado.append(esq[i])
            i += 1
        else:
            combinado.append(dir[j])
            j += 1

    while i < len(esq):
        combinado.append(esq[i])
        i += 1

    while j < len(dir):
        combinado.append(dir[j])
        j += 1

    return combinado

# Exemplo de uso
numeros = [14, 13, 6, 7, 239, 11, 54]
resultado_ordenado = ordenar_merge(numeros)
print(resultado_ordenado)
