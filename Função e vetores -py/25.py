def Sem7():
    i = 0
    lista = []
    while i < 100:
        if i%7 == 0 or i%10==7:
            i = i + 1
        else:
            lista.append(i)
            i = i + 1
    return lista
print(Sem7())
