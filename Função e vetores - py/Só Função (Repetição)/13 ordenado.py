def ordenado(a,b,c):
    if a>b:
        if b>c:
            print("Ordenado",c,b,a)
        if c>b: 
            print("Ordenado",b,c,a)
    
    if b>a:
        if a>c:
            print("Ordenado",c,a,b)
        if c>a:
            print("Ordenado",a,c,b)
    if c>a:
        if a>b:
            print("Ordenado",b,a,c)
        if c>a:
            print("Ordenado",a,b,c)
        


print(ordenado(4,1,5))