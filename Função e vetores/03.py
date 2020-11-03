def Vetor(lista):
	print ("Digite os elementos da lista")
	
	i = 0
	while i < 5:
		n = int(input( "Digite um numero: " ))
		lista.append(n)
		i = i + 1
    

def quadrado(a):
    c = []
    i = 0
    while i < 5:
        c.append(a[i]**2)
        i = i + 1
    return c

a = []
print(Vetor(a))
#print(a)
print(a)
c = quadrado(a)
print(c)

