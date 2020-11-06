def funçao(n):
    i = 1
    soma = 0
    while i <= n:
        var = (i**2+1)/(i+3)
        soma = soma + var
        i = i + 1
    return soma

print(funçao(1))
print(funçao(2))
print(funçao(3))
print(funçao(4))
print(funçao(5))
print(funçao(6))
print(funçao(7))
print(funçao(8))
print(funçao(9))
print(funçao(10))