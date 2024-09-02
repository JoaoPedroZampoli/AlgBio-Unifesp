Lista1 = ["Ana", "Thiago", "Mariana", "Manuel", "Regina", "Reginaldo"]

def CompararTamanho(Lista):
    Resultado = 0
    for i in range(len(Lista)):
        if(len(Lista[i]) > 5):
            Resultado += 1
    print(Resultado)


CompararTamanho(Lista1)