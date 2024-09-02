#Em química, o pH de uma solução aquosa é uma medida da sua acidez.
#Os Valores de pH variam entre 0 e 14. Soluções ácidas tem pH menor que 7. 
#Soluções básicas tem pH maior que 7. Soluções neutras tem pH igual a 7. 
#Escreva duas funções que recebem um número correspondente ao pH de uma solução aquosa e exibem na tela o tipo de solução (algo como “A solução é ácida”).

ph = int(input("Digite um valor de pH: "))

if(ph < 7 and ph >= 0):
    print("Solução Ácida")
elif(ph > 7 and ph <= 14):
    print("Solução Básica")
elif(ph == 7):
    print("pH Neutro")
else:
    print("pH Inválido!")