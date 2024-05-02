def RemoveDuplicados(Lista):
    if len(Lista) == 0:
        print("Lista Vazia!")
        return
    else:
        print("Remoção de Duplicados: ")
        i = 0
        while i < len(Lista):
            j = i + 1
            while j < len(Lista):
                if(Lista[i] == Lista[j]):
                    Lista.remove(Lista[j])
                else:
                    j += 1
            i += 1

#Uma forma que achei melhor de fazer, no entanto, não sei se poderia criar outra lista
def RemoveDuplicadosMelhor(Lista):
    TamanhoLista = len(Lista)
    if(TamanhoLista == 0):
        print("Lista Vazia!")
        return
    else:
        ListaSemDuplicados = []
        for i in range(TamanhoLista):
            if (Lista[i] not in ListaSemDuplicados):
                ListaSemDuplicados.append(Lista[i])
        print("Remoção de Duplicados: ")
        print(ListaSemDuplicados)

def MaiorMenorLista(Lista):
    UltimaPosicao = len(Lista)
    if(UltimaPosicao == 0):
        print("Lista Vazia!")
        return
    else:
        MaiorValor = Lista[0]
        MenorValor = Lista[0]

        for i in range(1,UltimaPosicao):
            if(MaiorValor < Lista[i]):
                MaiorValor = Lista[i]
            elif(MenorValor > Lista[i]):
                MenorValor = Lista[i]
        print("\nMaior Valor = ",MaiorValor)
        print("Menor Valor = ",MenorValor)
        print("Ultima Posição = ",UltimaPosicao)

Lista = [4, 8, 9, 6, 2, 4, 7, 3, 2, 0, 1, 2]
RemoveDuplicados(Lista)
#RemoveDuplicadosMelhor(Lista)
MaiorMenorLista(Lista)