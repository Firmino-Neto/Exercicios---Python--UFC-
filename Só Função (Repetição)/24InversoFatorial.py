def Fatorial(n):
    fat = 1
    i = 1
    while i<=n: 
        fat = fat * i
        i = i+1
    return fat

def inverso(n):
    i = 1
    soma = 0
    while i<=n:
        soma = soma + 1/Fatorial(i)
        i = i + 1
    return 1+soma

n = 5
print(Fatorial(n))
print(inverso(n))