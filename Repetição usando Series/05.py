

n = int(input("Digite o vaor de N: "))
i = 1
soma = 1 
while i < n:
    
    termo = 1/(2*i)   #Contagem começa em zero
    soma = soma + termo
    i = i + 1
    
print(soma)