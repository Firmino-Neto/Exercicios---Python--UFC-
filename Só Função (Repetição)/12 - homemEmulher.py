
print("1 - homens ||| 0 - Mulheres")
M = 0
H = 1

def PesoIdeal(altura,sexo):
    ideal_0M = 62.1*altura - 44.7
    ideal_1H = 72.7*altura - 58
    
    if sexo == 0:
        return ideal_0M
        
    if sexo == 1:
        return ideal_1H
    
    else:
        print("Digite valores validos")

print(PesoIdeal(1.70,0))
    
    
