def Vetor(lista,codigo):
    i = 1
    while i <= 5:
        if codigo == 0:
            print("Programa finalizado")
            break
    
        if codigo >2:
            print("Opção inválida")
            break

        n = int(input( "Digite um numero: " ))
        lista.append(n)
        i = i + 1
    return ('')

def imprimirLista(lista,codigo):
    tam = len( lista )
    i = 0

    while i < tam:
        if codigo == 1:
            return lista
            
        if codigo == 2:
            return lista[::-1]

lista = []
codigo = int(input( "Codigo de ordem de impressão - " ))

print(Vetor(lista,codigo))
print(imprimirLista(lista,codigo))