lista = []
for c in range(1, 6):
    numeros = int(input(f'Digite um valor para a Posição {c}: '))
    lista += [numeros]
c = 0
print('Você digitou os valores ', end='')
for n in lista:
    c += 1
    print(n, end=', ' if c < 5 else '.')
print(f'\nO maior valor digitado foi {max(lista)}, o qual apareceu nas posições ', end='')
for pos, n in enumerate(lista):
        if n == max(lista):
            print(pos, end=' ')
print(f'\nO menor valor digitado foi {min(lista)}, o qual apareceu nas posições ', end='')
for pos, n in enumerate(lista):
    if n == min(lista):
            print(pos, end=' ')

