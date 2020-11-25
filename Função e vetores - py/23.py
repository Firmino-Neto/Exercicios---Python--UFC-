def Vetor( lista, tam ):
	print ("Digite os elementos da lista")	
	contador = 0
	while contador < tam:
		numero = int(input("Digite um numero: "))
		lista.append( numero )
		contador = contador + 1

def Escalar( a, b ):
    i = 0
    soma = 0
    while i<len(a):
        soma = soma + a[i]*b[i]
        i = i + 1
    return soma

#Codigo principal [chamar função]
a = []
b = []

#Fazer CompLista = 10
Vetor(a,5)
Vetor(b,5)

print(a)
print(b)

print("o produto escalar dos dois vetores é",Escalar(a,b))