def SomaDigitos(Numero):
    TamanhoNumero = len(Numero)

    Soma = 0

    for i in range(TamanhoNumero):
        Soma += int(Numero[i])
    print("Soma dos Dígitos =",Soma)

Numero = input("Digite um Número: ")
SomaDigitos(Numero)


