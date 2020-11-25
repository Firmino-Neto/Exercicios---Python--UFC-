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
    lista.append(maior)

def MenorElemento(lista):
    menor = lista[ 0 ]
    i = 1
    while i < len(lista):
        if lista[ i ] < menor:
            menor = lista[ i ]
        i = i + 1
    lista.append(menor)

def Media(lista):
    i = 0
    tam = len(lista)
    soma = 0
    while i<= tam-1:
        soma = soma + lista[i]
        i = i +1
    lista.append(soma/tam)
#Codigo Principal [Retorno da funções]

lista = []
Vetor( lista )

print(MaiorElemento(lista))
print(MenorElemento(lista))
print(Media(lista))

print(lista)