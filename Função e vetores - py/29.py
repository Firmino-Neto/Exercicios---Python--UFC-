
def Vetor(lista):
	print ("Digite os elementos da lista")	
	contador = 0
	while contador < 6:
		numero = int(input("Digite um numero: "))
		lista.append( numero )
		contador = contador + 1

def Par_Impar(lista):
    i = 0
    listaPar = []
    listaImpar = []
    
    somaPar = 0
    contaPar = 0
    
    SomaImpar = 0
    contaImpar = 0
    while i < len(lista):
        if lista[i]%2 == 0:
            listaPar.append(lista[i])
            somaPar = somaPar + lista[i]
            contaPar += 1
            i = i + 1
    
        else:
            listaImpar.append(lista[i])
            SomaImpar += lista[i]
            contaImpar += 1 
            i = i + 1
    print("Pares Digitados:",listaPar)
    print("Quantidade de pares:",contaPar)
    print('')
    print("Impares Digitados:",listaImpar)
    print("Quantidade de impares:",contaImpar)
    
    return ('')

lista = []
print(Vetor(lista))

print(Par_Impar(lista))
            
        

