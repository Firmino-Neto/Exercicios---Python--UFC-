

print("Escolha uma letra das opções para começar")
print("")
print("   1 - média aritmetica")
print("   2 - média ponderada")
print("   3 - média harmonica")
print("")


def nota(a,b,c):
    escolha = int(input("Digite a opção de nota desejada: "))
    if escolha == 1:
        mediaA = (a+b+c)/3
        print("media =",(a+b+c)/3)
        return mediaA
        
    if escolha == 2:
        mediaP = (5*a+3*b+2*c)/10
        print("media =",(a+b+c)/3)
        return mediaP
        
    if escolha == 3:
        mediaH = 3/(1/a+1/b+1/c)
        print("media =",(a+b+c)/3)
        return mediaH
    else:
        print("Digite uma opção deseja")
        escolha = int(input("Digite a opção de nota desejada: "))
        
print(nota(9,8,7))
        
        
        
        
