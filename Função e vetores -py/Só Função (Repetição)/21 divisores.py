def divisor(n):
    i = 1
    Div = []
    while i<= n//2+1:
        if n%i == 0:
            Div.append(i)
            i = i + 1
        else:
            i = i + 1
    Div.append(n)

    return Div
    
print(16*'==')
print(6*' ',"Lista de divisores")
print(divisor(100))
print(16*'==')