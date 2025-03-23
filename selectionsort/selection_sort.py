def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        posicao = i
        for j in range(i + 1, n):
            if arr[j] < arr[posicao]:
                posicao = j
        arr[i], arr[posicao] = arr[posicao], arr[i]  

arr = [23, 9, 8, 11, 13, 55, 4, 41, 12, 33]

print("Vetor antes de ordenar:")
print(arr)
selection_sort(arr)
print("\nVetor depois de ordenar com Selection Sort:")
print(arr)
