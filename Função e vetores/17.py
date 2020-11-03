def Vetor(lista):
	print ("Digite os elementos da lista")
	i = 1
	while i <= 5:
		n = int(input( "Digite um numero: " ))
		lista.append(n)
		i = i + 1
	return ('')

def Negativo(lista):
    i = 0
    tam = len(lista)
    while i<= tam - 1:
        if lista[i]<0:
            lista[i]=0
            i = i +1
        else:
            i = i + 1
    return ''


#Codigo principal
lista = []
Vetor( lista )

print(Negativo(lista))
print(lista)
