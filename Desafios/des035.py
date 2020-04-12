km = float(input('Qual é a distância da viagem em Km? '))
if km <= 200:
    print('Você deve pagar R${:.1f}!'.format(0.50*km))
else:
    print('Você deve pagar R${:.1f}!'.format(0.45*km))
