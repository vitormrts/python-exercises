from datetime import date
anoatual = date.today().year
anonasc = int(input('Em que ano você nasceu? '))
idade = anoatual - anonasc
print(f'Você se encaixa na categoria', end=' ')
if idade <= 9:
    print('MIRIM.')
elif idade <= 14:
    print('INFANTIL.')
elif idade <= 19:
    print('JÚNIOR.')
elif idade <= 25:
    print('SÊNIOR.')
else:
    print('MASTER.')