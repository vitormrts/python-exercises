import math
num = float(input('Digite um número: '))
print('A raiz quadrada de {:.0f} é {:.2f};'.format(num, math.sqrt(num)))
print('O dobro de {:.0f} é {:.0f};'.format(num, num*2))
print('O quadrado de {:.0f} é {:.0f}'.format(num, math.pow(num, 2)))
