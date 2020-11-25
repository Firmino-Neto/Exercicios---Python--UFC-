def Ordenada():
    print ("Digite os elementos da lista: ")	
    i = 0
    c = []
    while i < 11:
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
    print(c)
    
    i = 0
    des = []
    while i < len(c):
        if i <= 5:
            des.append(c[i])
            i = i + 1

        else:
            des.append(c[5-i])
            i = i + 1
           
       
            
        
    print(des)
        

print(Ordenada())
