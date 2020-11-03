def Vetor(lista):
	print ("Digite os elementos da lista")
	i = 0
	while i <= 10:
		n = int(input( "Digite um numero: " ))
		lista.append(n)
		i = i + 1
	return ('')
    
def contarPar(a):
    i = 0
    cont = 0
    while i<=10:
        if a[i]%2==0:
            cont = cont + 1
            i = i + 1
        else: 
            i = i + 1
    return cont

    
a = []
print(Vetor(a))
print(a) 

c = contarPar(a)
print("O vetor possui %i valores pares" %(c))