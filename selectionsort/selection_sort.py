def selection_sort(arr):
    n = len(arr)
    
    for i in range(n - 1):
        posicao = i
        for j in range(i + 1, n):
            if arr[j] < arr[posicao]:
                posicao = j
        arr[i], arr[posicao] = arr[posicao], arr[i]  

arr = [40, 1, 23, 20, 67, 44, 9, 18, 0, 99]

print("Vetor antes de ordenar:")
print(arr)

selection_sort(arr)

print("\nVetor depois de ordenar com Selection Sort:")
print(arr)
