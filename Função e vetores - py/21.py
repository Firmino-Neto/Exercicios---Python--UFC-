def Vetor( lista, tam ):
	print ("Digite os elementos da lista")	
	contador = 0
	while contador < tam:
		numero = int(input("Digite um numero: "))
		lista.append( numero )
		contador = contador + 1


def subtraiVetor(a,b):
	c = []
	i = 0
	while i < len(a):
	    subtracao = a[i]-b[i]
	    c.append(subtracao)
	    i = i + 1
	
	return c


#Codigo principal [chamar função]

a = []
b = []

#Fazer CompLista = 10
CompLista = int(input( "Digite a quantidade de numeros: " ))

Vetor(a,CompLista)
Vetor(b,CompLista)

print(a)
print(b)

print(subtraiVetor(a,b))
