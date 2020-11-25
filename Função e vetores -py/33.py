def Vetor(lista):
	print ("Digite os elementos da lista: ")	
	contador = 0
	while contador < 5:
		numero = int(input("Digite um numero: "))
		lista.append( numero )
		contador = contador + 1

def Compacto(a):
    i = 0
    c = []
    while i<len(a):
        if a[i] == 0:
            i = i + 1
        else:
            c.append(a[i])
            i = i + 1
    return c

a = []
Vetor(a)
print(Compacto(a))

