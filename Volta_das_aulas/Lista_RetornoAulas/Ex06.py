Vetor = [1,1,2,3,5,8,13,21,34]
VetorNegativo = [-1,-1,-2,-3,-5,-8,-13,-21,-34]

print("Vetor:")
for i in range(len(VetorNegativo)-1):
    j = i+1
    Distancia = VetorNegativo[j]-VetorNegativo[i]
    if(Distancia < 0):
        Distancia *= -1
    print("Distância do próximo elemento: ", Distancia)

print("\nVetor Negativo:")
for i in range(len(VetorNegativo)-1):
    j = i+1
    Distancia = VetorNegativo[j]-VetorNegativo[i]
    if(Distancia < 0):
        Distancia *= -1
    print("Distância do próximo elemento: ", Distancia)