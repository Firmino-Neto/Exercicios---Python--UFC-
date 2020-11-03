def Vetor(lista):
	print ("Digite os elementos da lista")	
	contador = 0
	while contador < 10:
		numero = int(input("Digite um numero: "))
		lista.append( numero )
		contador = contador + 1

def uniao(a,b):
    c = []
    i = 0
    while i < len(a):
        if a[i] not in c:
            c.append(a[i])
        i = i + 1
    d = c
    i = 0
    while i < len(b):
        if b[i] not in d:
            d.append(b[i]) 
        i = i + 1
    return d

a = []
b = []

print(Vetor(a))
print(Vetor(b))

print(uniao(a,b))