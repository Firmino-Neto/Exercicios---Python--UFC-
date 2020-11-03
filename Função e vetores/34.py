def Vetor():
    print ("Digite os elementos da lista: ")	
    i = 0
    lista = []
    while i < 5:
        n = int(input("Digite o numero: "))

        if n not in lista:
            lista.append(n)
            i = i + 1
        
        else:
            i = i + 1
    return lista

print(Vetor())
