num = int(input('Digite um número inteiro: '))
contador = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[1;34m{}'.format(c), end=' ')
        contador = contador + 1
    else:
        print('\033[1;31m{}'.format(c), end=' ')
if contador == 2:
    resposta = 'é PRIMO'
else:
    resposta = 'não é PRIMO'
print('\n\033[mO número {} é divisível por {} números e, por isso, {}.'.format(num, contador, resposta))