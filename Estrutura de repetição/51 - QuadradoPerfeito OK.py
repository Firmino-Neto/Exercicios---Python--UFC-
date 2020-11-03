
valor = int(input('Digite um numero positivo maior que zero: '))
soma = 1
cont = 0
impar = 1

if valor>=0:
    while cont < int(valor**(1/2)-1):
        impar = impar + 2
        soma = soma + impar
        cont = cont + 1
    
if soma == valor:
    print("É quadrado é perfeito")
else:
    if valor<0:
        print("[ERROR] Digite um número positivo")
    else:
        print("NÃO é quadrado perfeito")



"""
valor = int(input('Digite um numero: '))
soma = 1
cont = 0
impar = 1

while cont < int(valor**(1/2)-1):
    impar = impar + 2
    soma = soma + impar
    cont = cont + 1
    
if soma == valor:
    print("É quadrado é perfeito")
else:
    print("NÃO é quadrado perfeito")
"""
