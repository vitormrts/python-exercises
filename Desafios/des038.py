salario = float(input('Qual é o valor, em reais, de seu salário? '))
if salario > 1250:
    print('Seu novo salário será de R${:.1f}'.format(salario*1.1))
else:
    print('Seu novo salário será de R${:.1f}.'.format(salario*1.15))