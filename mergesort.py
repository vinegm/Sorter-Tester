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
    resultado = np.array([], dtype=int)
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