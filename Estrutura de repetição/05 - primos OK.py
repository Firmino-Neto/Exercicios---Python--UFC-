n = int(input("Digite o número para saber se o é primo: "))

if n<=0:
    print("O Número digitado é inválido, tente novamente")
    n = int(input("Digite o número para saber se o é primo: "))

multiplo=0

for i in range (2,n//2+1):
    if (n%i ==0):
        #print("É Múltiplo de",i)
        multiplo += 1
    
if multiplo ==0:
    print("É primo")
else:
    print("Não é primo")
    #print("Não é primo, pois tem",multiplo, "multiplos de 2 até", n )



"""
fatores = []
n = int(input("digite um número para saber se é primo: "))

for i in range(1,n+1):
    if n%i ==0:
        fatores.append(i)
        if len(fatores) > 2: 
            print("%i não é primo"%(n))
            break
if len(fatores) == 2:
    print("%i é primo"%(n))

"""
