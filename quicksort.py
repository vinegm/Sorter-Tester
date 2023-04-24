import numpy as np
from numpy import random as rd
import timeit
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

testCases = [vetor1, vetor2, vetor3, vetor4, vetor5, vetor6, vetor7, vetor8]