#Parte 1
def Vetor(n,m):
    #i = 0
    lista1 = []
    lista2 = []
    
    if n >= 10000:
        n = int(input("Digite um numero menor que 10.000: "))
        
    while n//10 > 0 or m//10 >0:
        resto1 = n%10
        lista1.append(resto1)
        
        resto2 = m%10
        lista2.append(resto2)
        
        quociente1 = n//10
        n = quociente1
        
        quociente2 = m//10
        m = quociente2
        
    lista1.append(n%10)
    lista2.append(m%10)
    
    print ("Algarismos que compoem os numeros")
    print(lista1,lista2)
  
    j = 0
    soma = 0
    while j < len(lista1) or j < len(lista2):
        soma = soma + (lista1[j] + lista2[j])*10**j
        j = j + 1 

    return soma

n = int(input("Digite n: "))
m = int(input("Digite m: "))
print(Vetor(n,m))


#Parte 2