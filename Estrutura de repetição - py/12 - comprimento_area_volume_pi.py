

cont = 1
demo1 = 1 
demo2 = 1 
soma = 0

n = int(input("Digite o numero de interações: "))
r = int(input("Digite o valor do raio: "))
while cont <= n:
    if cont%2 == 0:
        soma = soma - (1)/(demo1**3)
    else:
        soma = soma + (1)/(demo1**3)
    
    demo1 = demo1 + 2 
    demo2 = demo1
    cont = cont + 1

pi = (soma*32)**(1/3)

comprimento = 2*pi*r

area = pi*r**2

Vesfera = (4*pi*r**3)/3

print(pi)
print("O comprimento é:%.2f"%(comprimento))
print("A area é:%.2f"%(area))
print("O volume da esfera é:%.2f"%(Vesfera))
