# Exercício 01
# Simulações de Monte Carlo são uma classe de algoritmos que usam números aleatórios para obter resultados numéricos.
# Eles encontraram uso prático em uma gama de aplicações biomédicas.  
# !!!!!Considere o polinômio de segunda ordem tal como F(x) = x² + 1!!!!!
# Utilize o método de monte carlo para estimar a área sob a curva de f(x) no intervalo de x[1,4] e y[0,17]

# A) Escreva uma função que solicite ao user o número de pontos a ser utilizado e calculue o valor de phi conforme o enunciado.
# Não é permitido usar comandos for ou while.
# B) Escreva uma rotina em python que faça o plot do resultado da simulação de acordo com a imagem acima
import numpy as np
import matplotlib.pyplot as plt

def MonteCarlo():
    NumeroPontos = int(input("Escreva o número de pontos a serem utilizados: "))
    X = np.random.uniform(1, 4, NumeroPontos)
    Y = np.random.uniform(0, 17, NumeroPontos)

    FunctionX = X**2 + 1

    PontosAbaixoCurva = Y < FunctionX

    CurvaX = np.linspace(1, 4, 500)
    CurvaY = CurvaX**2 + 1

    Area = (np.sum(PontosAbaixoCurva) / NumeroPontos) * (4 - 1) * (17 - 0)

    plt.plot(CurvaX, CurvaY, color="black", linewidth=3)
    plt.scatter(X[PontosAbaixoCurva], Y[PontosAbaixoCurva], color="red", s=20)
    plt.scatter(X[~PontosAbaixoCurva], Y[~PontosAbaixoCurva], color="blue", s=20)

    plt.xlabel("Eixo X")
    plt.ylabel("Eixo Y")
    plt.title(f"Valor de Área Aproximado: {Area:.3f}")
    plt.show()

    return Area

AreaEstimada = MonteCarlo()
print("Valor da Área Aproximada: ", AreaEstimada)