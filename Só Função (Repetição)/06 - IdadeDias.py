def idade(anos,mes,dia):
    
    Idade_dias = 365*anos + mes*30 + dia
    return 'A idade em dia é',Idade_dias

print(idade(20,5,3))
