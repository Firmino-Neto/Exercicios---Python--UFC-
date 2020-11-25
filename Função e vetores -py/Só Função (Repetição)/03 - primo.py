

def primo(n):
    cont = 0
    for i in range(1,n):
        if n%i == 0:
            cont = cont + 1 

    if cont==1:
        print(i+1,"É primo")
    else:
        print(i+1,"NÃO primo")
"""
for k in range(1,10):
        print(k,"-->",primo(k))
        print("")
"""
