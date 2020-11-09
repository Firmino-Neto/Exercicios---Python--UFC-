N = int(input("Digite o vaor de N: "))
i = 1
soma = 0 
while i<=N:
    termo = (-1)**(i+1) *(1/i) 
    soma = soma + termo
    i = i + 1
    
print("Valor de S é",soma)

