def Vetor(lista):
    #print ("Digite os elementos da lista")
    i = 0
    while i < 50:
        n = (i+5*i)%(i+1)
        lista.append(n)
        i = i + 1

lista = []
print(Vetor(lista))
print(lista)
