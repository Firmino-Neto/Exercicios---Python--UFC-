

def harmonico(n):
    soma = 0
    for i in range(1,n+1):
        h = 1/i
        soma = soma + h
        soma = soma
        i = i+1
    print(soma)

print(harmonico(6))
