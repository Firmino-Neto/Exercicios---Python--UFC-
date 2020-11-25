def Vetor(lista):
	print ("Digite os elementos da lista")
	i = 0
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
        if lista[ i ] > maior:
            maior = lista[ i ]
            indice = i
        i = i + 1
    print(maior)
    print("Posiçao do maior elemento da lista:",indice)    

   

#Codigo Principal [Retorno da funções]

lista = []
Vetor( lista )
print(lista)
print(MaiorElemento(lista))

