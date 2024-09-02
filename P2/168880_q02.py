# Exercício 02
# Crie uma função na qual se calcula o valor do seno hiperbólico a partir da série de Taylor (50 primeiros termos)
# e Cosseno Hiperbólico a partir da seguinte identidade: Fórmula na prova
# Não pode utilizar comandos de loops (for e/ou while).  Utilizar a função factorial da biblioteca scipy

import numpy as np
from scipy.special import factorial

def TaylorSenH(X, NumeroTermos):
    N = np.arange(0, NumeroTermos)
    Termos = (X ** (2 * N + 1)) / factorial(2 * N + 1)
    return np.sum(Termos)

X = float(input("Digite o valor de X: "))
XSenH = TaylorSenH(X, 50)
print(f'Seno Hiperbólico({X}) ≈ {XSenH:.3f}')

def TaylorCosH(X, NumeroTermos):
    n = np.arange(0, NumeroTermos)
    Termos = (X ** (2 * n)) / factorial(2 * n)
    return np.sum(Termos)

# Testando a função
XCosH = TaylorCosH(X, 50)
print(f'Cosseno Hiperbólico({X}) ≈ {XCosH:.3f}')

Checagem = XCosH**2 - XSenH**2
print(f'CosH^2({X}) - SenH^2({X}) = {Checagem:.3f} (deve ser próximo de 1)')





