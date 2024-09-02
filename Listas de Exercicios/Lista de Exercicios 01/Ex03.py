#Escreva um script que leia a quantidade de dias, horas, minutos e segundos para o usuário. Calcule o total em segundos.

Dias = int(input("Digite a quantidade de dias: "))
Horas = int(input("Digite a quantidade de horas: "))
Minutos = int(input("Digite a quantidade de minutos: "))
Segundos = int(input("Digite a quantidade de segundos: "))

Total = Segundos + ((Minutos + ((Horas + (Dias * 24))*60))*60)

print(f"{Dias} Dias, {Horas} Horas, {Minutos} Minutos, {Segundos} Segundos em Segundos é igual a: {Total} s")