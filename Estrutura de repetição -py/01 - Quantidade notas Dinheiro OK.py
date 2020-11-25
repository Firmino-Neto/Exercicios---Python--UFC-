"""
01 - Faça um programa que apresente um palpite para um jogo da loteria. Nossa loteria
consiste de seis números inteiros aleatórios entre 0 e 100.
No Brasil existem notas de 1, 2, 5, 10, 20, 50 e 100 reais. Faça um programa que, dado
um valor inteiro em reais, mostre a menor combinação de notas existente para esse
valor.
"""



print("="*50)
print(15*" ","FIRMINO ACOUNT")
print("="*50)

valor = int(input('Digite o Valor que deseja sacar: '))

valorTotal=valor
notas=100
TotalNotas=0

while True:
    if valorTotal>=notas:
        valorTotal = valorTotal - notas
        TotalNotas += 1
    else:
        if TotalNotas>0:
            print("Total de %d de %d" %(TotalNotas,notas))
        if notas==100:
            notas=50
            
        elif notas==50:
            notas=20
            
        elif notas==20:
            notas=10
            
        elif notas==10:
            notas=5
            
        elif notas==5:
            notas=2
            
        elif notas==2:
            notas=1
            
        TotalNotas=0
        if valorTotal==0:
            break



            
