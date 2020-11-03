def Vetor(lista):
    print ("Digite os elementos da lista")
    i = 0
    while i <6:
        n = int(input( "Digite um numero par: " ))
        if n%2 == 0:
            lista.append(n)
            i = i + 1
        else:
            n = int(input( "Digite um numero par: " ))
	        

def OrdemInversa(lista):
    i = 1
    tam = len(lista)
    listaInversa=[] 
    while i<=tam:
        listaInversa.append(lista[tam-i])
        i = i +1
    return (listaInversa)

lista = []
Vetor( lista )
print(lista)
print(OrdemInversa(lista))
