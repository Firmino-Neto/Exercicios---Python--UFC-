

print("O n-ésimo termo da sequência de Fibonacci.")
print()
n = int(input("Digite a posição do termo da sequência: "))

Fn2=1
Fn1=1
cont = 2

if n==1 or n==2:
    print(1)
    
else:
    while cont<n:
   
        Fn = Fn2 + Fn1
        Fn1 = Fn2
        Fn2 = Fn
        cont = cont + 1
        
    print("O %d° termo procurado da sequência é %d"% (cont,Fn))
    
