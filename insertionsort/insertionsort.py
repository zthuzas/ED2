def insertionsort(array):
    n = len(array)
    for i in range(1, n):
        chave = array[i]
        j = i - 1
        while j >= 0 and array[j] > chave:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = chave
        
array = [3, 12, 5, 7, 1, 9, 2]

print("Vetor antes de ordenar:")
print(array)
insertionsort(array)
print("Vetor depois de ordenar:")
print(array)
