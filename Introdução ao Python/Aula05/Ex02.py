def Hipotenusa(a,b):
    H = (a**2+b**2)**0.5
    return (H)

a = int(input("Cateto A: "))
b = int(input("Cateto B: "))

print("A Hipotenusa é: " + str(Hipotenusa(a,b)))