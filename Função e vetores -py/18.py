def Vetor(lista):
	print ("Digite os elementos da lista")
	i = 1
	while i <= 5:
		n = int(input( "Digite um numero: " ))
		lista.append(n)
		i = i + 1
	return ('')

def verificaMultiplo( lista,x):
    tam = len( lista )
    i = 0
    cont = 0
    while i < tam:
        if lista[ i ]%x == 0:
            cont = cont + 1
            print("multiplo de %i -> "%(x),lista[i]) 
        i = i + 1
    return cont

#Codigo principal
lista = []
Vetor( lista )
print("Quantidade de multiplos:",verificaMultiplo(lista,4))
