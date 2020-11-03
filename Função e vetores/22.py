def Vetor( lista, tam ):
	print ("Digite os elementos da lista")	
	contador = 0
	while contador < tam:
		numero = int(input("Digite um numero: "))
		lista.append( numero )
		contador = contador + 1


def Seleciona(a,b):
	c = []
	i = 0
	while i < 20:
	    if i%2==0:
	        c.append(a[i//2])
	        i = i + 1
	    else:
	        c.append(b[i//2])
	        i = i + 1
	return c


#Codigo principal [chamar função]

a = []
b = []

#Fazer CompLista = 10
Vetor(a,10)
Vetor(b,10)

print(a)
print(b)

print(Seleciona(a,b))