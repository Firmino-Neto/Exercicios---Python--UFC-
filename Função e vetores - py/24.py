def Aluno(listaNumero,listaAltura):
    i = 0
    
    while i < 3:
        num = int(input("Digite numero do aluno: "))
        altura = int(input("Digite a altura do aluno: "))
        listaNumero.append(num)
        listaAltura.append(altura)
        
        c = [listaNumero[i],listaAltura[i]]
        #print(c)
        i = i + 1
    print("Lista de numeros:",listaNumero)
    print("Lista de alturas:",listaAltura)

def MaiorElemento(listaAltura,listaNumero):
    maior = listaAltura[ 0 ]
    i = 1
    indice = 0
    while i < len(listaAltura):
        if listaAltura[ i ] > maior:
            maior = listaAltura[ i ]
            indice = i
        i = i + 1
    return (maior, listaNumero[indice])

def MenorElemento(listaAltura,listaNumero):
    menor = listaAltura[ 0 ]
    i = 1
    indice = 0
    while i < len(listaAltura):
        if listaAltura[ i ] < menor:
            menor = listaAltura[ i ]
            indice = i
        i = i + 1
    return (menor,listaNumero[indice])


		
listaNumero = []
listaAltura = []

print(Aluno(listaNumero,listaAltura))

print(MaiorElemento(listaAltura,listaNumero))
print(MenorElemento(listaAltura,listaNumero))