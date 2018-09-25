from random import randint

def escolhedia():
    rand_seg = (randint(0,15)/100)
    rand_ter = (randint(15,20)/100)
    rand_qua = (randint(20,25)/100)
    rand_qui = (randint(25,35)/100)
    rand_sex = (randint(35,50)/100)
    rand_fds = (randint(60,100)/100)

    dia = [rand_seg,rand_ter,rand_qua,rand_qui,rand_sex,rand_fds]
    rand = randint(0,5)
    return dia[rand]

def feriado():
    rand = randint(0,5)
    return rand

def printall(segunda,terca,quarta,quinta,sexta,fds):
    print("segunda-feira : ", segunda)
    print("terça-feira : ", terca)
    print("quarta-feira : ", quarta)
    print("quinta-feira : ", quinta)
    print("sexta-feira : ", sexta)
    print("fins de semana : ", fds)



def simule():
    carros = 1000
    segunda = 0
    terca = 0
    quarta = 0
    quinta = 0
    sexta = 0
    fds = 0

    for i in range (60):
        dia = escolhedia()
        feri = feriado()
        if (dia >= 0 and dia <= 0.15 and feri == 0):
            segunda += carros + (carros*dia)
            terca += carros
            quarta += carros
            quinta += carros
            sexta += carros
            fds += carros
        elif (dia > 0.15 and dia <= 0.20 and feri == 0):
            segunda += carros
            terca += carros + (carros*dia)
            quarta += carros
            quinta += carros
            sexta += carros
            fds += carros
        elif (dia > 0.20 and dia <= 0.25 and feri == 0):
            segunda += carros
            terca += carros
            quarta += carros + (carros*dia)
            quinta += carros
            sexta += carros
            fds += carros
        elif (dia > 0.25 and dia <= 0.35 and feri == 0):
            segunda += carros
            terca += carros
            quarta += carros
            quinta += carros + (carros*dia)
            sexta += carros
            fds += carros
        elif (dia > 0.35 and dia <= 0.50 and feri == 0):
            segunda += carros
            terca += carros
            quarta += carros
            quinta += carros
            sexta += carros + (carros*dia)
            fds += carros
        elif (dia > 0.60 and dia <=1):
            segunda += carros
            terca += carros
            quarta += carros
            quinta += carros
            sexta += carros
            fds -= carros*(dia-1)
        else:
            segunda += carros
            terca += carros
            quarta += carros
            quinta += carros
            sexta += carros
            fds += carros

    printall(segunda,terca,quarta,quinta,sexta,fds)

simule()
