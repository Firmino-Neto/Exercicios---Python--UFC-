def Vetor(lista):
    print ("Digite os elementos da lista")	
    contador = 0
    while contador < n:
        numero = int(input("Digite um numero: "))
        lista.append( numero )

        i = 0
        mult = 0
        indice = 1
        while i<numero:
            if lista[i] % indice == 0:
                mult = mult +1
                i = i + 1
                indice += 1
        if mult == 2:
            print(lista[i],i)
            i = i + 1
            indice += 1
        else:
            i = i + 1
            indice += 1

        contador = contador + 1
        numero = int(input("Digite um numero: "))
		

        return ('')
n = int(input("Digite o tamanho do vetor: "))

lista = []
print(Vetor(lista))
