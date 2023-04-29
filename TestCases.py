import numpy as np
from numpy import random as rd
import random

# ESCREVER MELHORES TESTES!!!!!!!!!!!!!!!!!!!!!!!!!
def test_cases():
    # Para testar: Lista de números em ordem aleatória.
    cenario1 = list(range(1, 101))
    random.shuffle(cenario1)

    # Para testar: Uma lista que já está ordenada.
    cenario2 = list(range(1, 101))

    # Para testar: Uma lista classificada em ordem decrescente.
    cenario3 = list(range(1, 101))
    cenario3.reverse()

    # Para testar: Uma lista contendo elementos repetidos.
    cenario4 = list(range(1, 101))
    repeated_numbers = random.sample(cenario4, 50)
    cenario4 = np.append(cenario4, repeated_numbers)
    random.shuffle(cenario4)

    # Para testar: Uma lista vazia.
    cenario5 = np.array([])

    # Para testar: Uma lista contendo apenas um elemento.
    cenario6 = np.array([5])

    # Para testar: Uma lista contendo um elemento repetido muitas vezes.
    cenario7 = list(range(1, 51))
    repeated_number = random.randint(1, 50)
    cenario7 = np.append(cenario7, ([repeated_number]*50))
    random.shuffle(cenario7)

    # Para testar: Uma lista longa.
    cenario8 = rd.randint(0, 10_000, 1_000)

    testCases = [cenario1, cenario2, cenario3, cenario4, cenario5, cenario6, cenario7, cenario8]
    return testCases
