Vetor = [1,1,2,3,5,8,13,21,34,55,89,144]

def CalculoMedia(Vetor):
    for i in range(len(Vetor)-1):
        Media = 0
        Media += Vetor[i]
    return(Media/len(Vetor))

def CalculoMediana(Vetor):
    Tamanho = int(len(Vetor))
    if (len(Vetor) % 2 == 0):
        Mediana = (Vetor[int(((Tamanho/2) - 1))] + Vetor[int((Tamanho/2))])/2
    else:
        Mediana = Vetor[int(Tamanho/2)]
    return Mediana

print("Média = ", CalculoMedia(Vetor))
print("Mediana = ", CalculoMediana(Vetor))

