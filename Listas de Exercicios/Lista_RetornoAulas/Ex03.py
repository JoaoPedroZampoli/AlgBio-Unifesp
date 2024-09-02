#Definir listas ou permitir usuário a escrever os elementos delas?
Lista1 = ["Ana", "Thiago", "Mariana", "Manuel", "Regina"]
Lista2 = ["Mariana", "Regina", "Letícia"]
Lista3 = []

TamanhoLista1 = len(Lista1)
TamanhoLista2 = len(Lista2)

for i in range(TamanhoLista1):
    for j in range(TamanhoLista2):
        if(Lista1[i] == Lista2[j]):
            Lista3.append(Lista1[i])

print(Lista3)