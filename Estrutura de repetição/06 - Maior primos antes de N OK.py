print("=======================================================")
print("Programa imprimi o primo mais proximo de um dado numero")
print("=======================================================")
numero = int(input("Digite um número maior ou igual a 2: "))
cont = 1
primos = []

for i in range(2,numero+1):
    for j in range (2,i): 
        if i%j == 0:
            break
        cont = cont + 1
    else:
        primos.append(i)

if i not in primos:
    print("O primo mais de %d é o %d" %(numero,primos[-1]))

else:
    if numero==2:
        print("Não há primos anterior a esse número")
    else:
        print("O primo mais de %d é o %d" %(numero,primos[-2]))
    
