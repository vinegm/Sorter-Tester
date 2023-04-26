import time
from datetime import timedelta


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