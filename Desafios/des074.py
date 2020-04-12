cont = 0
cont18 = 0
conthomem = 0
contmulher = 0
continuar = ''
while True:
    cont += 1
    print('='*40)
    print(' CADASTRE UMA PESSOA')
    print('='*40)
    idade = int(input('Idade: '))
    while idade < 0:
        idade = int(input('\033[1;31mOPÇÃO INVÁLIDA\033[m\nIdade:'))
    if idade > 18:
        cont18 += 1
    sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    while sexo not in 'MF':
        sexo = str(input('\033[1;31mOPÇÃO INVÁLIDA\033[m\nSexo [M/F]:')).strip().upper()[0]
    if sexo in 'Mm':
        conthomem += 1
    if sexo in 'Ff' and idade < 20:
        contmulher += 1
    print('='*40)
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar in 'Nn':
        break
    while continuar not in 'Ss':
        continuar = str(input('\033[1;31mOPÇÃO INVÁLIDA\033[m\nQuer continuar? [S/N]')).strip().upper()[0]
print(f'Você cadastrou {cont} pessoa(s).\n{cont18} pessoas possuem mais de 18 anos.\n{contmulher} mulheres tem menos de 20 anos.')