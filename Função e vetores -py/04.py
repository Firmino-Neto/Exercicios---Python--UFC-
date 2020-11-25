def Vetor(lista):
	print ("Digite os elementos da lista")
	i = 0
	while i < 5:
		n = int(input( "Digite um numero: " ))
		lista.append(n)
		i = i + 1
	return ('')
    
def XY(a):
    X = int(input("Digite uma posição na lista entre 0 e 8: " ))
    Y = int(input("Digite uma posição na lista entre 0 e 8: " ))
    soma = a[X]+a[Y]
    return soma

    
a = []

print(Vetor(a))
print(a) 

c = XY(a)
print(c)