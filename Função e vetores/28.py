def Vetor(lista):
	print ("Digite os elementos da lista")
	i = 1
	while i <= 10:
		n = int(input( "Digite um numero: " ))
		lista.append(n)
		i = i + 1
	return ('')

def ParImpar(lista):
    i = 0
    par = []
    impar = []
    while i < len(lista):
        if lista[i]%2 == 0:
            par.append(lista[i])
            i = i + 1
        else:
            impar.append(lista[i])
            i = i + 1
    return par,impar 

lista = []
print(Vetor(lista))
print(ParImpar(lista))