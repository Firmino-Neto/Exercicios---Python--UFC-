
#Supondo numeros positivos.
print("==== Transformando decimal em binario ====")
print("")
numero = int(input("Digite um número inteiro positivo: "))

pos = 0 
soma = 0
m = numero

while numero>=1:
    resto = numero%2
    numero = numero//2
    resto = resto*10**(pos)
    soma = soma + resto
    pos = pos + 1
    
print("A representação de %i em binario é %i" %(m,soma))

