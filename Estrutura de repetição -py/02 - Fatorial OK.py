
N = int(input("Digite um número inteiro maior que zero: "))

cont = 1 
fatorial = 1 

while cont<=N:
    fatorial = fatorial*cont
    cont+=1 
print("%d! = %d "%(N,fatorial))

