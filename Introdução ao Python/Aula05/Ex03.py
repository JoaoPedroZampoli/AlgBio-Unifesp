def Soma(*a):
    S = 0
    for i in a:
        S += i
    return S

print(Soma(1,2,3,4,5,6))