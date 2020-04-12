from time import sleep
km = float(input('Qual é a velocidade, em km/h, que você está andando? '))
sleep(1)
print('PROCESSANDO...')
sleep(1)
print('.')
sleep(1)
print('.')
sleep(1)
print('.')
sleep(2)
m = (km-80)*7
if km <= 80:
    print('Você está dentro da velocidade permitida.')
else:
    print(f'Você está acima da velocidade. Portanto, terá que pagar uma multa de R${m:.1f}')