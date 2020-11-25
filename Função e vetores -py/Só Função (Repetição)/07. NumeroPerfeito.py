

def perfeito(n):
    soma=0
    for i in range(1,n//2+1):
        if n%i == 0:
            soma += i
            i += 1
    if soma==n:
        return 1
    else:
        return 0
print(perfeito(7))
