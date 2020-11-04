

cont = 2 
n = int(input("Digite numero: "))
demo1 = 1 
demo2 = 1 
soma = 1 
numerador = 3

while cont <=n:
    if cont%4 == 0 or (cont+1)%4 == 0:
        soma = soma - (numerador**2)/(demo1**3)
    else:
        soma = soma + (numerador**2)/(demo1**3)
    
    aux = demo1
    demo1 = demo1 + demo2 
    demo2 = aux
    numerador = numerador + 2
    cont = cont + 1 
    
print("%.5f" %(soma))
