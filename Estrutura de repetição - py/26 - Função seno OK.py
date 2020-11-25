
import math

x = int(input("Digite o ângulo em graus: "))

k = 1 
soma = 0
rad = 3.1415*(x/180)

for i in range(1,20,2):
    soma = soma + k*pow(rad,i)/(math.factorial(i))  #Conta cada termo e soma
    k = k *(-1)         #Muda o sinal
    
print(soma)

""" 
========== Teste ============

x = 90 ---> 1.0
x = 45 ---> 0.7071067811865475

========== Teste ============
"""




"""
#Denominador é da forma 2k-1

n  = int(input("digite um numero: "))

cont = 1 
fat = 1 

while cont<=n:
    fat = fat*cont
    cont+=1 
print("%d! = %d "%(n,fat))


2 maneira (TENTAR FAZER)
-> JUNTAR ESSA PARTE DE CIMA + PARTE DE BAIXO 
 
Tentar juntar essas duas coisa
x = int(input("Digite o valor de x: "))

rad = 3.1415*(x/180)

fat = 1 
seno = 0
cont = 0
    
for i in range(1,20,2):
    fat = fat*i
    seno = seno + (x**i)/(fatorial(2*i-1))

    print(fat,i)
    
"""
