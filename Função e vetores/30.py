def Vetor(lista):
	print ("Digite os elementos da lista")	
	contador = 0
	while contador < 10:
		numero = int(input("Digite um numero: "))
		lista.append( numero )
		contador = contador + 1

def interseçao(a,b):
    i = 0
    Inter = []
    while i < len(a):
        j = 0
        while j < len(b):
            if a[i] == b[j] and a[i] not in Inter:
                Inter.append(a[i])
            j = j + 1
        i = i + 1

    return Inter

a = []
b = []

print(Vetor(a))
print(Vetor(b))

print(interseçao(a,b))