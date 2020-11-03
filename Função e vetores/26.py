def Vetor(lista):
	print ("Digite os elementos da lista")	
	contador = 0
	while contador < n:
		numero = int(input("Digite um numero: "))
		lista.append( numero )
		contador = contador + 1
	
def DesvioPadrao(lista):
    i = 0
    somaMedia = 0
    while i < len(lista):
        somaMedia = somaMedia + lista[i]
        i = i + 1
    m = somaMedia/len(lista)

    res = 0
    i = 0
    while i < len(lista):
        res = res + (lista[i] - m)**2
        i = i + 1
        
    Desvio = 1/(n-1)*res 
    return Desvio
    #return m


#Codigo de chamada das funções
#Digite n = 10, para efeito da questão
n = int(input("Digite o valor de n: "))

lista = []
print(Vetor(lista))
print(lista)

print(DesvioPadrao(lista))







