from bisect import bisect_left


def insertion_sort(vetor):
  for i in range(1, len(vetor)):
    chave = vetor[i]
    # bisect_left eh uma funcao built-in python
    # que retorna o index onde o valor CHAVE
    # deve ser inserido no vetor de forma que a ordem seja mantida 
    j = bisect_left(vetor, chave, 0, i)
    # Empurramos o restante do vetor para a direita e inserimos o valor
    # CHAVE na posicao correta
    vetor[j+1:i+1] = vetor[j:i]
    vetor[j] = chave
  return vetor