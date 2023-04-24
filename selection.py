import numpy as np
from numpy import random as rd
import time 
from datetime import timedelta #para o output tempo ficar 00:00:00.000000

# Para testar: Lista de números em ordem aleatória.
vetor1 = np.array([8, 5, 1, 7, 9, 4, 10, 3, 6, 2])

# Para testar: Uma lista que já está ordenada.
vetor2 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Para testar: Uma lista classificada em ordem decrescente.
vetor3 = np.array([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])

# Para testar: Uma lista contendo elementos repetidos.
vetor4 = np.array([8, 5, 1, 7, 9, 4, 10, 3, 6, 2, 8, 5, 1])

# Para testar: Uma lista vazia.
vetor5 = np.array([])

# Para testar: Uma lista contendo apenas um elemento.
vetor6 = np.array([5])

# Para testar: Uma lista contendo um elemento repetido muitas vezes.
vetor7 = np.array([6, 9, 6, 7, 6, 5, 6, 6, 2, 6])

# Para testar: Uma lista longa.
vetor8 = rd.randint(0, 1000, 100)

# Para testar: Uma lista longa.
vetor9 = rd.randint(0, 1000, 1000)

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

# só colocar a lista nos dados e rezar
def calcula_tempo(vetor):
  start_time = time.monotonic() #começa a contagem do tempo percorrido
  vetorOrdenado = selectionSort(vetor)
  end_time = time.monotonic() #termina contagem do tempo percorrido
  print("Saída: ")
  print(vetorOrdenado)
  print("\nTempo de Execução: ")
  print(timedelta(seconds=end_time - start_time)) #printa contagem
  
#foi usado clock monotonico para ter tempo fracional

print(">>> Vetor 1 <<<")
print("Entrada: ")
print(vetor1)
calcula_tempo(vetor1)

