
def grau2(a,b,c):
    delta = b**2-4*a*c
    if delta==0:
        raiz1 =(-b/(2*a))
        raiz2 =(-b/(2*a))
        return("raiz1=",raiz1," and raiz2=",raiz2)
    
    if delta>0:
        raiz1 =(- b + delta**(1/2))/(2*a)
        raiz2 =(- b - delta**(1/2))/(2*a)
        return("raiz1=",raiz1," and raiz2=",raiz2)

    if delta<0:
        print("Não existe raizes reais")
    
    #return delta,raiz1,raiz2

print(grau2(1,5,6))
