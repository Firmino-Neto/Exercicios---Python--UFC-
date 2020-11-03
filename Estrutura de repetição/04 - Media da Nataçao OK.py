
print(" ")
print(" ===== Notas do nadador =====")

lista = []
for i in range(1,9):
    n = lista.append (float(input("Digite nota %i: "%(i))))
lista.remove(min(lista))
lista.remove(max(lista))

soma = 0.0 
for j in range(len(lista)):
    soma = soma + lista[j]
print("A media do nadador é",float(soma/6.0))
print(soma)
