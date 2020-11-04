

n = input("Digite o binario: ")
bin = n[::-1]

exp = 0
soma = 0
for i in bin:
    i = int(i)
    dec = i*2**exp
    soma = soma + dec
    exp = exp + 1
    
print('decimal correspondente:',soma)
