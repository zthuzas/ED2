def bubblesort(array):
    n = len(array)
    iteracoes = 0
    for i in range(n - 1):
        for j in range(n - 1 - i):
            iteracoes += 1
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return iteracoes
                