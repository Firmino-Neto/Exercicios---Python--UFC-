
print("Programa verifica se um numero ou não perfeito")

n = int(input("Digite um número inteiro positivo: "))
soma = 0

for cont in range(1,n+1):
    if n%cont == 0:
        soma = soma + cont
        cont = cont + 1
#print(soma)
        
if soma == 2*n:
    print("O %d é um número perfeito!"%(n))
else:
    print("O %d NÃO é um número perfeito!"%(n))

