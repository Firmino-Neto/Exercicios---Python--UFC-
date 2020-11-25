def Vetor(lista):
	print ("Digite os elementos da lista: ")	
	contador = 0
	while contador < 5:
		numero = int(input("Digite um numero: "))
		lista.append( numero )
		contador = contador + 1
	
def soma(x,y):
    i = 0
    VetorSoma = []
    while i<len(x):
        soma = x[i]+y[i]
        VetorSoma.append(soma)
        i = i + 1
    return VetorSoma

def produto(x,y):
    i = 0
    VetorProduto = []
    while i<len(x):
        produto = x[i] * y[i]
        VetorProduto.append(produto)
        i = i + 1
    return VetorProduto

def diferença(x,y):
    i = 0
    VetorDiferença = []
    while i<len(x):
        diferença = x[i] - y[i]
        VetorDiferença.append(diferença)
        i = i + 1
    return VetorDiferença
    
def interseçao(x,y):
    i = 0
    Inter = []
    while i < len(x):
        j = 0
        while j < len(y):
            if x[i] == y[j] and x[i] not in Inter:
                Inter.append(x[i])
            j = j + 1
        i = i + 1

    return Inter

def uniao(x,y):
    c = []
    i = 0
    while i < len(x):
        if x[i] not in c:
            c.append(x[i])
        i = i + 1
    d = c
    i = 0
    while i < len(y):
        if y[i] not in d:
            d.append(y[i]) 
        i = i + 1
    return d
  
x = []
y = []

Vetor(x)
Vetor(y)

print(soma(x,y))
print(produto(x,y))
print(diferença(x,y))
print(interseçao(x,y))
print(uniao(x,y))
