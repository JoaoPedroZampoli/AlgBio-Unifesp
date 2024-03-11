#Crie um script em Python que solicite o nome, altura e peso
#de uma pessoa e mostre a seguinte mensagem: “João tem 90
#quilos e altura de 1.78 e portanto o IMC é de 28.4”.

Nome = input("Digite o Nome: ")
Altura = float(input("Digite a Altura: "))
Peso = float(input("Digite o Peso: "))

IMC = Peso/Altura**2

print(f"{Nome} tem {Peso:.2f} quilos e Altura de {Altura:.2f}")