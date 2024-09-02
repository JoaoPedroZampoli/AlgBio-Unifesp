#Leia a temperatura em graus Celsius e converta para Fahrenheit.

TF =  float(input("Digite a Temperatura em Fahrenheit: "))

TC = (TF - 32) * 5/9

print(f"A Temperatura de {TF:.1f}°F é igual a {TC:.1f}°C")