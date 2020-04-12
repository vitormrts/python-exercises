from datetime import date
nascimento = int(input('Em que ano você nasceu? '))
anoatual = int(date.today().year)
idade = anoatual - nascimento
if idade == 18:
    print('Você precisa se alistar IMEDIATAMENTE!')
elif idade >= 19:
    deveria = 18 + nascimento
    tempo = anoatual - deveria
    print('Você já deveria estar alistado há {} ano(s).\nO seu alistamento foi em {}.'.format(tempo, deveria))
else:
    deve = (nascimento + 18) - anoatual
    print('Você deve se alistar em {} ano(s), ou seja, em {}. Até logo!'.format(deve, 18+nascimento))