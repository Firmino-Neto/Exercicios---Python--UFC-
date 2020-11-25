def Vetor(lista):
	print ("Digite os elementos da lista")
	i = 1
	while i <= 10:
		n = int(input( "Digite um numero: " ))
		lista.append(n)
		i = i + 1
	return ('')

def Negativo(lista):
    i = 0
    tam = len(lista)
    cont = 0
    while i<= tam - 1:
        if lista[i]<0:
            cont = cont + 1
            i = i +1
        else:
            i = i + 1
    return cont

def SomaPositivo(lista):
    i = 0
    tam = len(lista)
    soma = 0
    while i<= tam-1:
        if lista[i]>=0: 
            soma = soma + lista[i]
            i = i + 1
        else:
            i = i + 1
    return soma

#Código principal 

lista = []
Vetor( lista )
print(lista)

print("Quantidade de negatvios na lista:", Negativo(lista))
print("Soma dos pares:", SomaPositivo(lista))