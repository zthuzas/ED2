#import random

def selection_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        posicao = i

        for j in range(i + 1, n):
            if arr[j] < arr[posicao]:
                posicao = j

        if posicao != i:
            arr[i], arr[posicao] = arr[posicao], arr[i] 

def exibir_vetor(arr):
    print(" ".join(map(str, arr))) 

arr = [23, 9, 8, 11, 13, 55, 4, 41, 12, 33]

print("Vetor antes de ordenar:")
exibir_vetor(arr)
print()

selection_sort(arr)

print("Vetor depois de ordenar com Selection Sort:")
exibir_vetor(arr)
