
contador=0
soma=0
numero = 0

while numero>=0:
    
    numero = int(input("Digite um número: "))
    
    if numero>=0:
        soma = soma + numero 
        contador = contador + 1

if contador!=0:
    print(40*"=")
    print("A quantidade de números pares = %d" %(contador))
    print("A soma dos números pares digitados = %d" %(soma))
    print("A média do positivos é",soma/contador)
    print(40*"=")
else:
    print("Não foram digitados números positivos")
        
