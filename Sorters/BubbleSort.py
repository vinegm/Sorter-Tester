def bubble2_sort(vetor):           # Bolha com melhor desempenho   
    n = len(vetor)
    troca = True                   # Verifica tamanho do vetor.
    while troca:             # Enquanto houver troca, continua.  
        troca = False                  # Considera que troca pode não ocorrer.
        for i in range(n-1):           # Percorre para o final do vetor.
            if vetor[i] > vetor[i+1]:    # Verifica se a troca é necessária.
                vetor[i], vetor[i+1] = vetor[i+1], vetor[i]  # Realiza a troca.
                troca = True               # Sinaliza que houve troca. 
        n -= 1                         # Ajusta o tamanho do vetor a ser percorrido.   
    return vetor


def bubble2_sort_counting(vetor):   
    n = len(vetor)
    comparisons = 0
    swaps = 0
    troca = True
    while troca:
        troca = False
        for i in range(n-1):
            comparisons += 1
            if vetor[i] > vetor[i+1]:
                vetor[i], vetor[i+1] = vetor[i+1], vetor[i]
                troca = True
                swaps +=1
        n -= 1
    return vetor, comparisons, swaps