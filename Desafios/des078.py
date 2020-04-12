lanche = 'Hambúrger', 'Suco', 'Pizza', 'Pudim'
cont = 0
print('Eu vou comer', end=' ')
for comida in lanche:
    cont += 1
    print(comida, end=', ' if cont <= len(lanche)-1 else '.')
print('\nComi pra caramba! ')
print('.\n'
      '.\n'
      '.\n'
      '.\n'
      '.\n'
      '.\n')
print('Eu vou comer', end=' ')
for c in range(0, len(lanche)):
    print(lanche[c], end=', ' if c < len(lanche)-1 else '.')
print('\nComi pra caramba!')
print('.\n'
      '.\n'
      '.\n'
      '.\n'
      '.\n'
      '.\n')
for pos, comida in enumerate(lanche):
    print(f'{comida} na posição {pos}')
#sorted = mostra em ordem alfabetica
#index = posiçao


