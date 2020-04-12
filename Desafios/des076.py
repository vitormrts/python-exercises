resto1 = 0
resto2 = 0
resto3 = 0
resto4 = 0
qntd50 = 0
qntd20 = 0
qntd10 = 0
qntd1 = 0
vf = 0
valor = int(input('Qual valor você deseja sacar? R$'))
if valor >= 50:
    qntd50 = valor // 50
    valor %= 50
    print(f'{qntd50} cédulas de R$50.00')
if valor >= 20 and valor < 50:
    qntd20 = valor // 20
    valor %= 20
    print(f'{qntd20} cédulas de R$20.00')
if valor >= 10 and valor < 20:
    qntd10 = valor // 10
    valor %= 10
    print(f'{qntd10} cédulas de R$10.00')
if valor < 10 and valor != 0:
    qntd1 = valor // 1
    valor %= 1
    print(f'{qntd1} cédulas de R$1.00')
