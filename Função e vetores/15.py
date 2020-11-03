def Vetor(tam):
    print ("Digite os elementos da lista")
    i = 0
    lista = []
    while i < tam:
        n = int(input( "Digite elemento do vetor: " ))
        if n in lista:
            i = i + 1
        else:
            lista.append(n)
            i = i + 1 
            
    return (lista)

tam = int(input( "Digite o tamanho do vetor: " ))
print(Vetor(tam))

