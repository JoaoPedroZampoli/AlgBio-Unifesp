#Faça um script que calcule o aumento de salário. Ele deve solicitar o valor do salário e a porcentagem de aumento.
#Exiba o valor do aumento e do novo salário.

Salario = float(input("Digite o Salário Atual: R$ "))
PorcentoAumento = float(input('Digite a Porcentagem de Aumento (sem "%"): '))

NovoSalario = Salario * (PorcentoAumento + 100)/100
AumentoSalario = NovoSalario - Salario

print(f"O Valor do Novo Salário é de R$ {NovoSalario:.2f}")
print(f"O Aumento foi de R$ {AumentoSalario}")