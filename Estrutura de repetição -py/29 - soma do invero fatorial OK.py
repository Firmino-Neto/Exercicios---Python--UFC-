
print("Esse programa gera uma aproximação para a constante de Euler")

n = int(input("digite N: "))

i = 2
fatorial = 1
somaE = 1

#for i in range(1,n+1):

while i<=n:
    
    fatorial = fatorial * i
    somaE = somaE + 1/fatorial
    i = i + 1
    
print(somaE)
