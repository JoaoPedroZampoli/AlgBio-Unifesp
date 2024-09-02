#Crie um programa que imprima a sequência de Fibonacci até o décimo termo usando um loop for.
X = 0
Y = 1

print(X)
print(Y)
for i in range(8):
    Next = X+Y
    X = Y
    Y = Next
    print(Next)