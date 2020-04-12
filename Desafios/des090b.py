num = list()
par = list()
impar = list()
while True:
    num.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)
print(f'\nLista completa: {num}'
      f'\nLista de pares: {par}'
      f'\nLista de ímpares: {impar}')