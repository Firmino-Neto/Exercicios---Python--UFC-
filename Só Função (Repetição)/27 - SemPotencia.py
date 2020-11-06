
def mult(x,z):
    
    cont = 1
    produto = 1
    while cont <= z:
        
        if z==0:
            return 1
        
        if z>0:
            produto = produto*x
            cont = cont +1
           
        
        if z<0:
            produto = produto*1/x
            cont = cont +1
            
    return produto
print(mult(2,3))
        
