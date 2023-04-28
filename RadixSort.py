def index_sort(lista):
    if len(lista) < 1:
        return lista
    # determina o valor máximo e mínimo da lista
    valor_maximo = max(lista)
    valor_minimo = min(lista)

    # Cria uma lista com um índice para cada valor possívl na array, considerando os valores máximos e mínimos
    contadores = [0] * (valor_maximo - valor_minimo + 1)
    # Conta a ocorrência de cada valor na lista
    for valor in lista:
        contadores[valor - valor_minimo] += 1

    # Constrói a lista ordenada
    lista_ordenada = []
    for valor in range(valor_minimo, valor_maximo + 1):
        indice = valor - valor_minimo
        # Adiciona o valor na lista ordenada, o valor é adicionado de acordo com a quantidade de vezes que ele aparece na lista original
        lista_ordenada.extend([valor] * contadores[indice])

    return lista_ordenada