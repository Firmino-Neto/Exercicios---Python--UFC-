def Vetor(lista):
	print ("Digite os elementos da lista")
	i = 1
	while i <= 15:
		n = int(input( "Digite nota %i: " %(i)))
		lista.append(n)
		i = i + 1
	return ('')

def Media(lista):
    i = 0
    tam = len(lista)
    soma = 0
    while i<= tam-1:
        soma = soma + lista[i]
        i = i +1
    return soma/tam

lista = []
Vetor( lista )
print(lista)
print(Media(lista))