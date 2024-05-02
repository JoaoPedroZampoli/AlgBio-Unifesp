def Fatorial(Numero):
    Resultado = Numero
    for i in range(Numero-1, 0, -1):
        Resultado = Resultado*i

    return Resultado

def SenHiperbolico(Numero):
    Resultado = 0

    for N in range(0, 30):
        Resultado += (1/Fatorial((2*N+1))*pow(Numero,(2*N+1)))

    return Resultado

Numero = int(input("Digite um Valor: "))
print(SenHiperbolico(Numero))