# Utilizar estas funcões para calcular tempo para organizar

def quick_sort(array):
  sortedArray = quick_sorter_for_timing(array, 0, len(array)-1)
  return sortedArray

def particao_for_timing(array, first, last):
  # Utiliza o primeiro item do array como pivo
  pivot = array[first]

  # Utiliza o segundo item da lista como ponteiro menor, e ultimo item da lista como maior ponteiro
  low = first + 1
  high = last
  
  while True:
    
    # Percorre o array até encontrar um valor maior ou igual ao nosso pivo
    while low <= high and array[low] <= pivot:
      low += 1
    
    # Percorre o array até encontrar um valor menor ou igual ao nosso pivo
    while low <= high and array[high] >= pivot:
      high -= 1
    
    # Caso os ponteiros tenham se encontrado quebra o loop
    if high < low:
      break
    # Caso os ponteiros não tenham se encontrado, inverte os valores que eles estão apontando e continua o loop
    else:
      array[low], array[high] = array[high], array[low]

  # Inverte o pivo com o valor do maior ponteiro, colocando ele em seu local definitivo
  array[first], array[high] = array[high], array[first]
  # Retorna o valor do maior ponteiro para ser usado no dividir o array em dois
  return high


def quick_sorter_for_timing(array, first, last):
  # Continua ordenando a lista enquanto o ponteiro passado para a função não se encontrarem
  if first < last:
    # Procura o local para dividir e organizar a lista
    split= particao_for_timing(array, first, last)
    
    # Divide a lista em duas partes para organizar seus elementos
    quick_sorter_for_timing(array, first, split - 1)
    quick_sorter_for_timing(array, split + 1, last)

  return array


# Utilizar estas funcões para calcular quantidade de comparações e mudanças

def quick_sort_for_counting(array):
  comparisons = 0
  swaps = 0
  sortedArray, comparisons, swaps = quick_sorter_for_counting(array, 0, len(array)-1, comparisons, swaps)
  return sortedArray, comparisons, swaps

def particao_for_counting(array, first, last):
  # Utiliza o primeiro item do array como pivo
  pivot = array[first]

  comparisons = 0
  swaps = 0

  # Utiliza o segundo item da lista como ponteiro menor, e ultimo item da lista como maior ponteiro
  low = first + 1
  high = last
  
  while True:
    
    # Percorre o array até encontrar um valor maior ou igual ao nosso pivo
    while low <= high and array[low] <= pivot:
      low += 1
      comparisons += 1
    
    # Percorre o array até encontrar um valor menor ou igual ao nosso pivo
    while low <= high and array[high] >= pivot:
      high -= 1
      comparisons += 1
    
    # Caso os ponteiros tenham se encontrado quebra o loop
    if high < low:
      break
    # Caso os ponteiros não tenham se encontrado, inverte os valores que eles estão apontando e continua o loop
    else:
      array[low], array[high] = array[high], array[low]
      swaps += 1

  # Inverte o pivo com o valor do maior ponteiro, colocando ele em seu local definitivo
  array[first], array[high] = array[high], array[first]
  swaps += 1
  # Retorna o valor do maior ponteiro para ser usado no dividir o array em dois
  return high, comparisons, swaps


def quick_sorter_for_counting(array, first, last, comparisons, swaps):
  # Continua ordenando a lista enquanto o ponteiro passado para a função não se encontrarem
  if first < last:
    # Procura o local para dividir e organizar a lista
    split, comparisons, swaps = particao_for_counting(array, first, last)
    
    # Divide a lista em duas partes para organizar seus elementos
    split_left = quick_sorter_for_counting(array, first, split - 1, comparisons, swaps)
    split_right = quick_sorter_for_counting(array, split + 1, last, comparisons, swaps)

    # Soma as mudanças e comparações antes de retornar o valor
    comparisons += split_left[1] + split_right[1]
    swaps += split_left[2] + split_right[2]

  return array, comparisons, swaps