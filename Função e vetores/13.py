def Vetor(lista):
	print ("Digite os elementos da lista")
	i = 1
	while i <= 5:
		n = int(input( "Digite um numero: " ))
		lista.append(n)
		i = i + 1
	return ('')
    
def MaiorElemento(lista):
    maior = lista[ 0 ]
    i = 0
    indice = 0
    while i < len(lista):
        if lista[ i ] >= maior:
            maior = lista[ i ]
            indice = i
        i = i + 1
    return(indice)

def MenorElemento(lista):
    menor = lista[ 0 ]
    i = 1
    indice = 0
    while i < len(lista):
        if lista[ i ] <= menor:
            menor = lista[ i ]
            indice = i 
        i = i + 1
    return indice 

lista = []
Vetor( lista )

print("Posição do maior elemento:",MaiorElemento(lista))
print("Posição do menor elemento:",MenorElemento(lista))