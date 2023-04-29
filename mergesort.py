import numpy as np


def merge_sort(vetor):
    # Verifica se o vetor tem tamanho 1 ou 0 e retorna o vetor caso afirmativo
    if len(vetor) <= 1:
        return vetor
    
    # Divide o vetor em duas partes iguais 
    meio = len(vetor) // 2
    esquerda = merge_sort(vetor[:meio])
    direita = merge_sort(vetor[meio:])

    # Mescla as duas partes ordenadas em um vetor único
    return merge(esquerda, direita)


def merge(esquerda, direita):
    resultado = np.array([], dtype = int)
    i = j = 0

    #Compara os elementos de esquerda e direita e adiciona o menor ao resultado
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            resultado = np.append(resultado, esquerda[i])
            i += 1
        else:
            resultado = np.append(resultado, direita[j])
            j += 1

    # Adiciona o restante dos elementos de esquerda ou direita ao resultado
    resultado = np.append(resultado, esquerda[i:])
    resultado = np.append(resultado, direita[j:])
    
    return resultado


def merge_sort_counting(vetor):
    return merge_sorter_counting(vetor, 0, 0)


def merge_sorter_counting(vetor, comparisons, swaps):
    # Verifica se o vetor tem tamanho 1 ou 0 e retorna o vetor caso afirmativo
    if len(vetor) <= 1:
        return vetor, comparisons, swaps
    
    # Divide o vetor em duas partes iguais 
    meio = len(vetor) // 2
    esquerda = merge_sort_counting(vetor[:meio])
    direita = merge_sort_counting(vetor[meio:])

    # Mescla as duas partes ordenadas em um vetor único
    merged = merge_counting(esquerda[0], direita[0])

    comparisons += merged[1] + esquerda[1] + direita[1]
    swaps += merged[2] + esquerda[2] + direita[2]

    return merged[0], comparisons, swaps


def merge_counting(esquerda, direita):
    resultado = np.array([], dtype = int)
    i = j = 0

    comparisons = 0
    swaps = 0

    #Compara os elementos de esquerda e direita e adiciona o menor ao resultado
    while i < len(esquerda) and j < len(direita):
        comparisons += 1
        if esquerda[i] < direita[j]:
            resultado = np.append(resultado, esquerda[i])
            i += 1
            swaps += 1
        else:
            resultado = np.append(resultado, direita[j])
            j += 1
            swaps += 1

    # Adiciona o restante dos elementos de esquerda ou direita ao resultado
    resultado = np.append(resultado, esquerda[i:])
    resultado = np.append(resultado, direita[j:])
    swaps += 1  # This swap adder might be wrong/unecessary
    
    return resultado, comparisons, swaps
