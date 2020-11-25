def horario(hora,minuto):
    if hora>12 and hora<24:
        pm = hora - 12
        print('São %i:%i pm.' %(pm,minuto))
    if hora==24:
        print('São 00:%i am.' %(minuto))
    else:
        am = hora
        print('São %i:%i am.' %(hora,minuto))
    
hora = int(input("Digite a hora: "))
minuto = int(input("Digite os minutos: "))

horario(hora,minuto)