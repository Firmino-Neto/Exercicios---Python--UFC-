
N = int(input("Numero de interções: "))

i = 1
num = 0
lista = []

while i<N:
    num = num + 2**(i-1)
    i = i+1
    lista.append(num)
    
print(lista)
