import random 

#print("[0] --> pedra")
#print("[1] --> papel")
#print("[2] --> tesoura")

print("Você vai jogar agora pedra,papel ou tesoura !!!")

escolhaPC = ('pedra','papel','tesoura')
escolhaJog = ('pedra','papel','tesoura')
computador = random.randint(0,2)
print()

print('o computador escolhe:',escolhaPC[computador])
print()

jogador = (input("O jogador escolhe: "))

while jogador in escolhaJog:
    
    if escolhaPC[computador] == jogador:
        print ("Empate")
            
    elif escolhaPC[computador] == 'pedra' and jogador == 'papel':
        print("Computador ganha")
            
    elif escolhaPC[computador] == 'papel' and jogador == 'tesoura':
        print("Computador ganha")
            
    elif escolhaPC[computador] == 'tesoura' and jogador == 'pedra':
        print("Computador ganha")
    else:
        print("Jogador ganha")
    print()

    print (" ---- proxima rodada ----")
    print()
    print('o computador escolheu:',escolhaPC[computador])
    print()
    jogador = (input("escolha uma jogada: "))
    print()
    
if jogador not in escolhaJog:
        print ("Erro 404")
    
print()

print (" ---- proxima rodada ----")
print()
print('o computador escolheu:',escolhaPC[computador])
print()
jogador = (input("escolha uma jogada: "))
print()
