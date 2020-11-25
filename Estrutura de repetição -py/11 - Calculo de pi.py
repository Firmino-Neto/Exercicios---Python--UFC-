

cont = 1 
n = int(input("Digite numero de interações: "))
demo1 = 1 
demo2 = 0 
soma = 0

while cont <=n:
    if cont%2 == 0:
        soma = soma - (1)/(demo1**3)
    else:
        soma = soma + (1)/(demo1**3)
    
    demo1 = demo1 + 2
    demo2 = demo1
    cont = cont + 1
pi = (soma*32)**(1/3)
print ("O valor aproximado de pi:",pi)
