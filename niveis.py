player = str(input('Digite seu nome '))

def classificacao ():
    XP = int(input('Digite sua XP: '))
    if XP < 1000 :
        nivel = "Ferro"
    elif XP >= 1000 and XP <= 2000 :
        nivel = "Bronze"
    elif XP >= 2000 and XP <= 5000 :
        nivel = "Prata"
    elif XP >= 5001 and XP <= 7000 :
        nivel = "Ouro"
    elif XP >= 7001 and XP <= 8000 :
        nivel = "Platina"
    elif XP >= 8001 and XP <= 9000 :
        nivel = "Acendente"
    elif XP >= 9001 and XP <= 10000 :
        nivel = "Imortal"
    elif XP >= 10001 :
        nivel = "Radiante"
    else:
       nivel = "Valor não encontrado!"
       
    return nivel

nivel = classificacao()
    
print ("Olá " + player +", seu Rank é " + nivel)