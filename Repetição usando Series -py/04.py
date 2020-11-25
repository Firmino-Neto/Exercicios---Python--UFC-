
N = int(input("Digite o vaor de N: "))
i = 0
soma = 0 
while i<=N:
    termo = 1/(2*i+1)   #Contagem começa em zero
    soma = soma + (-1)**(i)*termo
    i = i + 1

pi = 4*soma

print("valor aproximado de pi é",pi)