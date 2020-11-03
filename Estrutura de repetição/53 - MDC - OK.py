

#10 = [10,5,2,1]
#20 = [20,10,5,4,5,2,1]
#MDC = 10

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))

if a>0 and b>0:
    while b!=0:
    
        if b==0: 
            print(a)
    
        else:
            resto = a % b
            a = b
            b = resto      
    print(a)



