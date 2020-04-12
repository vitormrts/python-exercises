from random import randint
from time import sleep


while True:
    def sorteia(lista):
        print('-='*30)
        print('Sorteando 5 valores da lista: ', end='')
        for c in range(0, 5):
            lista.append(randint(1, 10))
        sleep(0.5)
        for n in lista:
            print(n, end=' ')
            sleep(0.5)
        print()
    def somaPar(lista):
        par = list()
        soma = 0
        for n in lista:
            if n % 2 == 0:
                soma += n
                par += [n]
        print(soma)
    numeros = list()
    sorteia(numeros)
    print(f'Somando os pares de {numeros}, temos ', end='')
    somaPar(numeros)
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    numeros.clear()
    if resp == 'N':
        break
print('FINALIZANDO...')
