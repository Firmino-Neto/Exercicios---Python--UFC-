

n = int(input("digite um número inteiro positivo: "))
listaA = []
listaI = []
for i in range(1, n//2):
    if n%i == 0:
        valor = n//i
        a = [i,valor]
        #a2= [valor,i]
        if i not in listaA:
            listaI.append(i)
            listaA.append(valor)
        i = i+1

for k in range(0,len(listaI)):
    print([listaI[k],listaA[k]])
    
#print(listaA,listaI)


"""
n = int(input("Digite um número: "))

listaA = []
listaI = []

for i in range(1, n//2):
    if n%i == 0:
        valor = n//i
        a1 = [i,valor]
        a2 = [valor,i]
        if a1 not in listaA and a2 not in listaA:
            listaA.append(a1)
        i = i+1
        
print(listaA)

"""




