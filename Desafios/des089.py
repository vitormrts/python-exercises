lista = []
c = 0
c2 = 0
resposta = ''
while True:
    num = int(input('Digite um número: '))
    lista += [num]
    c += 1
    continuar = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    while continuar not in 'NS':
        continuar = str(input('\033[1;31mOPÇÃO INVÁLIDA\033[m\nQuer continuar? [S/N]')).upper().strip()[0]
    if continuar == 'N':
        break
lista.sort(reverse=True)
print(f'{c} números foram digitados.'
      f'\nA ordem decrescente desses números é ', end='')
for n in lista:
    c2 += 1
    print(n, end=', ' if c2 <= len(lista) - 1 else '.')
for n in lista:
    if lista.count(5) >= 1:
        resposta = '\nO número 5 faz parte da lista!'
    else:
        resposta = '\nO número 5 não apareceu.'
print(resposta)