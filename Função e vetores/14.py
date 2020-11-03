def Vetor(lista):
	print ("Digite os elementos da lista")
	i = 1
	while i <= 5:
		n = int(input( "Digite um numero: " ))
		lista.append(n)
		i = i + 1
	return ('')

def repete(lista):
    i = 0
    cont = 0
    while i<len(lista):
        if lista[i] in lista:
            cont = cont + 1
            i = i + 1
        else: 
            if cont > 1:
                print(lista[i])


lista = []
Vetor( lista )

print(repete(lista))
