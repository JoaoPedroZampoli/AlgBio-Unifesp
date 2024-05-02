#<24,9 = Peso Normal
#>25 e <29,9 = Sobrepeso
#>30 = Obesidade

Nome = input("Digite o Nome da Pessoa: ")
Sexo = input("Digite o Sexo da Pessoa: ")
Peso = float(input("Digite o Peso da Pessoa: "))
Altura = float(input("Digite a Altura da Pessoa: "))

IMC = Peso/(Altura*Altura)

print("\n\n1) Os dados digitados foram:")
print("Nome:",Nome,"\nSexo:",Sexo,"\nPeso:",Peso,"\nAltura:",Altura)
print("2) IMC = {:.2f}".format(IMC))
if(IMC < 25):
    print("3) Situação: Peso Normal")
elif(IMC > 25 and IMC < 30):
    print("3) Situação: Sobrepeso")
else:
    print("3) Situação: Obesidade")