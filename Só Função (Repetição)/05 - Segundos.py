
def tempo(seg):
    if seg>=0:
        hora = seg/3600
        minutos= seg/60
        segundos =seg
        
        return("horas = %i <-> minutos = %i <-> segundos = %i"%(hora, minutos, segundos))
        
    else:
        return "ERROR - Digite um valor válido"

print(tempo(360))
    
    
