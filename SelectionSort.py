def selectionSort(arr):
    for i in range(len(arr)):  # Itera sobre o array
        # Define o índice do elemento mínimo como o índice atual da iteração
        min_index = i
        # Itera sobre os elementos do array à direita do elemento atual
        for j in range(i+1, len(arr)):
            # Se o elemento atual for maior que o próximo elemento à direita, atualiza o índice do elemento mínimo
            if arr[j] < arr[min_index]:
                min_index = j
        # Troca o elemento atual pelo elemento mínimo
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr  # Retorna o array ordenado


def selectionSort_counting(arr):
    comparisons = 0
    changes = 0
    for i in range(len(arr)):  # Itera sobre o array
        # Define o índice do elemento mínimo como o índice atual da iteração
        min_index = i
        # Itera sobre os elementos do array à direita do elemento atual
        for j in range(i+1, len(arr)):
            # Se o elemento atual for maior que o próximo elemento à direita, atualiza o índice do elemento mínimo
            if arr[j] < arr[min_index]:
                min_index = j
            comparisons += 1
        # Troca o elemento atual pelo elemento mínimo
        arr[i], arr[min_index] = arr[min_index], arr[i]
        changes += 1
    return arr, comparisons, changes  # Retorna o array ordenado