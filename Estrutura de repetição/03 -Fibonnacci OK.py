#Exemplos: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377 ...
"""
import time
inicio =time.time()
"""
#Solução 1
print("O n-ésimo termo da sequência de Fibonacci.")
print()
n = int(input("Digite a posição do termo da sequência: "))

Fn2=1
Fn1=1
cont = 2

if n==1 or n==2:
    print(1)
    
else:
    while cont<n:
   
        Fn = Fn2 + Fn1
        Fn1 = Fn2
        Fn2 = Fn
        cont = cont + 1
        
    print("O %d° termo procurado da sequência é %d"% (cont,Fn))

#Solução 2

"""
print("N-ésimo termo da sequência de Fibonacci.")

def fibonacci(n):
    n2=1
    n1=1
    if n==1 or n==2:
        return 1 
    cont = 2
    while cont<n:
        termo = n2 + n1
        n1 = n2
        n2 = termo
        cont = cont + 1
    return termo

#Exemplo:
print("O termo procurado é",fibonacci(10))
"""

"""
fim =time.time()
intervalo = fim - inicio

print("==========================")
print("Tempo de execução:%.4f" %(intervalo))
print("==========================")
"""
