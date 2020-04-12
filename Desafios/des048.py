peso = float(input('Qual é o seu peso em KG? '))
altura = float(input('Qual é a sua altura em metros? '))
imc = peso/(altura**2)
print('Seu IMC é de {:.1f}.'.format(imc))
if imc <= 18.5:
    print('VISH! Você está abaixo do peso.')
elif imc <= 25:
    print('OBA! Você está no peso ideal, continue assim.')
elif imc <= 30:
    print('CUIDADO! Você está sobre o peso ideal.')
elif imc <= 40:
    print('Procure um nutricionista assim que puder, pois você está obeso. ')
else:
    print('Vá ao nutricionista! Você está com obesidade mórbida. ')