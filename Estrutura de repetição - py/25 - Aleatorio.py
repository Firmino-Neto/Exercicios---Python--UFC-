

import random 

aleatorio = random.randint(1,100)
jogador = random.randint(1,100)

tentivas = 1 

while aleatorio != jogador:
    jogador = random.randint(1,100)
    tentivas += 1
    
if aleatorio == jogador:
    print(jogador,aleatorio, tentivas)

if 1<=tentivas<=3:
    print("Muito sortudo")
if 6<=tentivas<=6:
    print("Sortudo")
if 7<=tentivas<=10:
    print("Normal")
if tentivas>11:
    print("Esforçado")
