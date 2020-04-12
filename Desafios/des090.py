continuar = ''
lista = []
listapar = []
listaimpar = []
while True:
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        listapar += [num]
    if num % 2 == 1:
        listaimpar += [num]
    continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('OPÇÃO INVÁLIDA.\nQuer continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break
lista = listapar + listaimpar
print(f'\nA lista completa é {lista}.'
      f'\nA lista de pares é {listapar}.'
      f'\nA lista de ímpares é {listaimpar}.')
