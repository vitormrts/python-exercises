s = 0
contador = 0
for c in range(1, 501, 2): #NÚMEROS ÍMPARES
    if c % 3 == 0:
       s = s + c
       contador = contador + 1
print('A soma desses {} valores é {}.'.format(contador, s))