def Vetor(lista):
	print ("Digite os elementos da lista")
	i = 1
	while i <= 10:
		n = int(input( "Digite um numero: " ))
		lista.append(n)
		i = i + 1
	return ('')
    
def MaiorElemento(lista):
    maior = lista[ 0 ]
    i = 1
    while i < len(lista):
        if lista[ i ] > maior:
            maior = lista[ i ]
        i = i + 1
    return maior

def MenorElemento(lista):
    menor = lista[ 0 ]
    i = 1
    while i < len(lista):
        if lista[ i ] < menor:
            menor = lista[ i ]
        i = i + 1
    return menor

#Codigo Principal [Retorno da funções]

lista = []
Vetor( lista )

print(MaiorElemento(lista))
print(MenorElemento(lista))