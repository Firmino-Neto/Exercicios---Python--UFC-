"""
Sabe-se que cada número da forma n3 é igual a
soma de n números ímpares consecutivos. Faça um
programa que receba o número n, e determine quais
os números ímpares consecutivos cuja soma seja igual a n3.


2 --> 3 + 5 -> 8
3 --> 7 + 9 + 11 -> 27 
"""

n = int(input("Digite um inteiro positivo maior ou igual a 2: "))

for i in range(1,n**3,2):
    cont = i
    soma = 0
    #print(i)
     
    for k in range(1,n+1):
        soma += cont
        cont += 2
        
    if soma == n**3:
        impar = i
        print("O numeros cuja a soma é n³")
        for j in range(1,n+1):
            print(impar)
            impar = impar + 2
        print("A soma dos numeros acima é",soma,"=",n,"^3")
        
