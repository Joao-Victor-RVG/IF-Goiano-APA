arr = [1, 5, 6, 2, 8, 3, 9, 7, 10, 12, 4]


def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)


def busca_binaria(arr, chave):
    baixo, alto = 0, len(arr) - 1
    while baixo <= alto:
        meio = (baixo + alto) // 2
        if arr[meio] == chave:
            return meio
        elif arr[meio] < chave:
            baixo = meio + 1
        else:
            alto = meio - 1
    return -1



def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def insertion_sort(arr):
    for i in range(1, len(arr)):
        chave = arr[i]
        j = i - 1
        while j >= 0 and chave < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = chave



def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivo = arr[len(arr) // 2]
    menores = [x for x in arr if x < pivo]
    iguais = [x for x in arr if x == pivo]
    maiores = [x for x in arr if x > pivo]
    return quicksort(menores) + iguais + quicksort(maiores)


def mergesort(arr):
    if len(arr) > 1:
        meio = len(arr) // 2
        esquerda = arr[:meio]
        direita = arr[meio:]
        mergesort(esquerda)
        mergesort(direita)
        i = j = k = 0
        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                arr[k] = esquerda[i]
                i += 1
            else:
                arr[k] = direita[j]
                j += 1
            k += 1
        while i < len(esquerda):
            arr[k] = esquerda[i]
            i += 1
            k += 1
        while j < len(direita):
            arr[k] = direita[j]
            j += 1
            k += 1