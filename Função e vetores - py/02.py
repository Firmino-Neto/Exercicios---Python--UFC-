def Vetor(lista):
	print ("Digite os elementos")
	
	i = 0
	while i < 6:
		n = int(input( "Digite um numero: " ))
		lista.append(n)
		i = i + 1

a = []
print(Vetor(a))
print(a)


