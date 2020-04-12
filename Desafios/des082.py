cont = 0
par = 0
lista = []
numeros = (int(input('Digite um número: ')),
           int(input('Digite um número: ')),
           int(input('Digite um número: ')),
           int(input('Digite um número: ')))
print(f'Você digitou os valores ', end='')
for n in numeros:
    print(n, end=' ')
print(f'\nO número 9 apareceu {numeros.count(9)} vezes.')
for n in numeros:
    if n % 2 == 0:
        cont += 1
        lista += [n]
if lista == []:
    print('Não há números pares.')
else:
    print(f'Há {cont} números pares, que são ', end='')
    for l in lista:
        print(l, end=' ')
if n == 3:
    print(f'\nO número 3 apareceu pela primeira vez na {numeros.index(3) + 1}ª posição.')
else:
    print('\nO número 3 não apareceu em nenhuma posição.')
