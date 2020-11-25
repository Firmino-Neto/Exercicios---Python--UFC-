
print("Soma dos múltiplos de 3 e NÃO multiplos de 7 menores que 1000")

soma = 0
cont = 1

while cont<100:
    if cont%3==0 and cont%7!=0:
        soma = soma + cont
    cont = cont +1
print(soma)



"""
def somaMil():
    soma = 0
    for i in range(1,1000):
        if i%3==0 and i%7!=0:
            soma = soma + i
    return soma


print("A soma é %d" %(somaMil()))    

"""
