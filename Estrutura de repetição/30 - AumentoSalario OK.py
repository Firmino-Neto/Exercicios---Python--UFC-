
Ano = int(input("Digite o ano para saber o seu salario anual apartir de 2006: "))

#salario de 2005 ---> 1000
#Salario de 2006 ---> 0.015*1000 + 1000
#Salario de 2006 ---> 2*(0.015)*1000 + 1000


cont  = 0 

while Ano>=2006:
    Ano = Ano - 1
    cont = cont + 1
    if Ano == 2006:
        salarioAnual = 1000 + 2**(cont)*(0.015*1000)
    
print("Seu salario é R$ %d" %(salarioAnual))





"""
======= Segunda Maneira =======

n = int(input("Quantidade de anos após começando em 2007: "))

salarioInicial = 1000 #salario de 2005
aumento = 0.015*1000 
salarioUm = salarioInicial + aumento #salario de 2006
#print(salario)

for i in range(0,n):
    ano = 2007 + i
    aumento = 2*aumento
    salarioAnual = 1000 + aumento
    print("Em %i o salario será de %i" %(ano, salarioAnual))
    i = i+1

"""
