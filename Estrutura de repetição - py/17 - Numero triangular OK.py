
n = int(input("Digite um número inteiro positivo: "))

contador = 1
num = 0

while num < n:
    num = contador*(contador+1)*(contador+2)
    contador = contador + 1
    
if num == n:
    print("O número %d É triangular"%(n))
else: 
    print("O número %d NÃO É triangular"%(n))
    
