#Me orientei por um codigo similar que encontrei na net depois de algumas tentativas sem sair nada ou
#pelo menos não o triangulo com os valores corretos. 

def Pascal(n):
    
    lista = [[1],[1,1]]
    i = 1
    while i < n:
        acrescimo = [1]
        
        for j in range(0,len(lista[i])-1):
            acrescimo += [ lista[i][j] + lista[i][j+1] ]
        acrescimo = acrescimo + [1]
        lista = lista + [acrescimo]
        i = i + 1
    return lista

n = int(input("Digite número de linhas: "))

res = Pascal(n)

i = 0 
while i < len(res):
    print(res[i])
    i = i + 1
