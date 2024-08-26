import random
import numpy as np

Qtd = int(input("Digite a quantidade de elementos do Vetor: "))
Vetor = random.sample(range(0, 100), Qtd)
print("Vetor =", Vetor)
print("Vetor Invertido =", repr(np.flip(Vetor)))