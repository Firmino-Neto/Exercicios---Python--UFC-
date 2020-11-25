from random import randint

def Vetor(lista):
    i = 1
    while i<10:
        lista.append(randint(0,50))
        i = i + 1

def ImparesDe_A(lista):
    i = 0
    B=[]
    while i<len(lista):
        if lista[i]%2 == 1:
            B.append(lista[i])
            i = i + 1
        else:
            i = i + 1
    return B

#Codigo principal
lista = []
Vetor( lista )
print(lista)
print(ImparesDe_A(lista))