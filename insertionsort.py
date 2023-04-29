def insert_sort(vetor):
  #comparacoes, atribuicoes = 0 , 0                       # VARIAVEIS PARA ATRIBUIR AS COMPARAÇÕES E ATRIBUIÇÕES

  for p in range(len(vetor)):                            # FOR PARA PERCORRER O VETOR
    elemento_atual = vetor[p]

    #if p > 0:                                           # VERIFICA SE O P É MAIOR QUE 0
      #comparacoes +=1                                   # INCREMENTA O CONTADOR DAS COMPARAÇÕES EM 1

    while p > 0  and vetor[p - 1] > elemento_atual:     # A OTIMIZAÇÃO FICA NESSA PARTE AQUI, CASO O VALOR DA POSIÇÃO ANTERIOR SEJA MENOR, ELE NÃO FAZ MAIS A COMPARAÇÃO POIS TEORICAMENTE O RESTANTE JÁ ESTA ORDENADO.
      vetor[p] = vetor[p - 1]                           # A POSIÇÃO ATUAL DO VETOR RECEBE O VALOR DA POSIÇÃO ANTERIOR
      #atribuicoes += 1                                  # INCREMENTA O CONTADOR DAS ATRIBUIÇÕES EM 1
      p -= 1                                            # DECREMENTA A VARIAVEL DE CONTROLE DO FOR

    vetor[p] = elemento_atual                           # VETOR NA POSIÇÃO P RECEBE VALOR DA VARIAVEL ELEMENTO_ATUAL
    #atribuicoes += 1                                    # INCREMENTA O CONTADOR DAS ATRIBUIÇÕES EM 1
  
  return vetor                                         # **IMPRIMI** Retorna O VETOR ORDENADO


def insert_sort_otimizado_counting(vetor):
  comparisons, swaps = 0 , 0                       # VARIAVEIS PARA ATRIBUIR AS COMPARAÇÕES E ATRIBUIÇÕES

  for p in range(len(vetor)):                            # FOR PARA PERCORRER O VETOR
    elemento_atual = vetor[p]

    if p > 0:                                           # VERIFICA SE O P É MAIOR QUE 0
      comparisons +=1                                   # INCREMENTA O CONTADOR DAS COMPARAÇÕES EM 1

    while p > 0  and vetor[p - 1] > elemento_atual:     # A OTIMIZAÇÃO FICA NESSA PARTE AQUI, CASO O VALOR DA POSIÇÃO ANTERIOR SEJA MENOR, ELE NÃO FAZ MAIS A COMPARAÇÃO POIS TEORICAMENTE O RESTANTE JÁ ESTA ORDENADO.
      vetor[p] = vetor[p - 1]                           # A POSIÇÃO ATUAL DO VETOR RECEBE O VALOR DA POSIÇÃO ANTERIOR
      swaps += 1                                  # INCREMENTA O CONTADOR DAS ATRIBUIÇÕES EM 1
      p -= 1                                            # DECREMENTA A VARIAVEL DE CONTROLE DO FOR

    vetor[p] = elemento_atual                           # VETOR NA POSIÇÃO P RECEBE VALOR DA VARIAVEL ELEMENTO_ATUAL
    swaps += 1                                    # INCREMENTA O CONTADOR DAS ATRIBUIÇÕES EM 1
  
  return vetor, comparisons, swaps