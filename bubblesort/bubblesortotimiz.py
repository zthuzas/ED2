def bubblesortotimiz(array):
    n = len(array)
    iteracoes = 0
    for i in range(n - 1):
        trocou = False
        for j in range(n - 1 - i):
            iteracoes += 1
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                trocou = True
        if not trocou:  
            break
    return iteracoes