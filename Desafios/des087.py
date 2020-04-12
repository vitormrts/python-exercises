lista = []
c = 0
c2 = 0
while True:
    num = int(input('Digite um valor: '))
    lista += [num]
    c += 1
    if c > 1:
        for pos, num in enumerate(lista):
            if num == lista[pos-1]:
                print('Valor duplicado! Não vou continuar...')
                del lista[pos]
    continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break
lista.sort()
print(f'A sequência dos valores digitados, em ordem crescente, é ', end='')
for s in lista:
    c2 += 1
    print(s, end=', ' if c2 < len(lista) else '.')
