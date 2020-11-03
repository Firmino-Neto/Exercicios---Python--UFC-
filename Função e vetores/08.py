def Vetor(lista):
	print ("Digite os elementos da lista")
	i = 0
	while i <6:
		n = int(input( "Digite um numero: " ))
		lista.append(n)
		i = i + 1
	return ('')

def OrdemInversa(lista):
    i = 1
    tam = len(lista) 
    while i<=tam:
        print(lista[tam-i])
        i = i +1
    return ('')

lista = []
Vetor( lista )
print(lista)
print(OrdemInversa(lista))
