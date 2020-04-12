frase = str(input('Digite uma frase: ').upper().strip())
frase1 = frase.replace(' ', '')
if frase[::-1] == frase:
    resposta = 'é um PALÍNDROMO'
else:
    resposta = 'não é um PALÍNDROMO'
print(f'O inverso de {frase} é {frase[::-1]}. Portanto, ela {resposta}. ')

