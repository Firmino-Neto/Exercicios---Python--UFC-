
n = int(input("Digite a quantidade de alunos: "))
alunos = []
cont = 0

while cont<n:
    nota = int(input("Inserir nota%i do aluno%i: " %(cont,cont)))
    alunos.append(nota)
    cont = cont + 1
    
print('Nota maxima -',max(alunos))
print('Nota minima - ',min(alunos))

Maior_Sete=0
Menor_Sete=0

for i in alunos:
    if i >= 7:
        Maior_Sete += 1
    else:
        Menor_Sete += 1
        
print('Quantidade de notas menor de 7,0:',Menor_Sete)
print('Quantidade de notas menor de 7,0:',Maior_Sete)

#Faça a media das notas da turma

#Exercicio extra: Pedir a quantidade de provas feitas na turma e imprimir maior, menor, media de cada aluno.
