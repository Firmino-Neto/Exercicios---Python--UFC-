
print("=============================================")
print ("Faça sua escolha Digitando a opção desejada:")
print ("    1 - Novo Salario retirando o Imposto")
print ("    2 - Novo Salario com aumento")
print ("    3 - Classificação salarial")
print("=============================================")
opcao = int(input( "Digite a oção desejada: " ))

while opcao < 1 or opcao > 3:
	print ("[WARNING] Opção inválida. Digite novamente")
	print ("---------------------------------------------")
	opcao = int(input("Digite a opção desejada: "))
    
if opcao ==1:
    
    salario = int(input("Digite seu salario: "))
    
    imposto = 0.0	
    
    if salario < 500:
        imposto = salario*0.05
        print("Seu novo salario livre de imposto é R$ %d" %(salario - imposto))
        
    elif salario >= 500 and salario <= 850:
    	imposto = salario*0.10
    	print("Seu novo salario livre de imposto é R$ %d" %(salario - imposto))
    else:
        imposto = salario*0.15
        print("Seu novo salario livre de imposto é R$ %d" %(salario - imposto))

if opcao==2:
    salario = int(input("Digite seu salario: "))
    
    if salario > 1500:
        aumento = 25
        print("Seu novo salario após o aumento é R$ %d" %(salario + aumento))
        
    elif salario >= 750 and salario <= 1500:
        aumento = 50
        print("Seu novo salario após o aumento é R$ %d" %(salario + aumento))
        
    elif salario >= 450 and salario < 750:
        aumento = 75
        print("Seu novo salario após o aumento é R$ %d" %(salario + aumento))
        
    else:
        aumento = 100
        print("Seu novo salario após o aumento é R$ %d" %(salario + aumento))

if opcao==3:
    
    salario = int(input("Digite seu salario: "))
    
    if salario <= 700:
        print("Funcionario mal remunerado")
    else:
        print("Funcionario bem remunerado")
    
