Nome = input("Digite o Nome: ")
Altura = float(input("Digite a Altura: "))
Peso = float(input("Digite o Peso (em kg): "))

IMC = Peso/Altura**2

print(f"O IMC do {Nome} é de: {IMC:.2f}")