
#Problema do número 3025


n = int(input("Digite um valor maior que mil: "))

i = 1

while i<=n:
    if i<n:
        a = i//100
        b = i%100
        c = (a + b)**2
        if c<n+1:
        #print (n,i,c)
            if c == i:
                print("Eureka",i)
        i = i+1
        if i<n//100:
            a = i//10
            b = i%10
            c = (a + b)**2
            if c<n+1:
            #print (n,i,c)
                if c == i:
                    print("Eureka",i)
            i = i+1
            
        #print(i)
    
"""
for i in range(1,n):
    if i < n:
        if i<n//100:
            a = i//10
            b = i%10
            c = (a + b)**2
            if c<n+1:
            #print (n,i,c)
                if c == i:
                    print("Eureka",i)
    i = i+1
    if n//10<i<n:
        d = i//10
        e = i%10
        f = (a + b)**2
        if c<n+1:
        #print (n,i,c)
            if f == i:
                print("Eureka",i)
    i = i+1
        
"""
    

# para valores menores que 100:
"""
 if i<100:
        a = i//10
        b = i%10
        c = (a + b)**2
        if c<n+1:
        #print (n,i,c)
            if c == i:
                print("Eureka",i)
    i = i+1

"""







    
