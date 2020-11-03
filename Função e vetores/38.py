def Ordenada():
    print ("Digite os elementos da lista: ")	
    i = 0
    c = []
    while i < 10:
        n = int(input("Digite um numero: "))
        if i == 0 or n > c[-1]:
            c.append(n)
            i = i + 1
        else:
            j = 0
            while j < len(c):
                if n <= c[j]:
                    c.insert(j,n)
                    break
                j = j + 1
            i = i + 1

    i = 0
    while i < len(c):
        print(c[i])
        i = i + 1

print(Ordenada())
            