def Vetor(A):
    A = [1, 0, 5, -2, -5, 7]
    print("O vetor é:",A)
    
    soma = A[0]+A[1]+A[5]
    print ("A soma de A[0] + A[1] + A[5]:",soma)
    
    A[4]=100
    return A
        
a = []
print(Vetor(a))
