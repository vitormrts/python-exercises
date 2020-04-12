from random import randint
from time import sleep
from operator import itemgetter
cont = 0
c = 0
jogadas = {'Jogador Nº1': randint(1, 6),
           'Jogador Nº2': randint(1, 6),
           'Jogador Nº3': randint(1, 6),
           'Jogador Nº4': randint(1, 6)}
ranking = dict()
print('Valores sorteados: ')
for k, v in jogadas.items():
    print(f'O {k} tirou {v}')
    sleep(1)
ranking = sorted(jogadas.items(), key=itemgetter(1), reverse=True)
for k, v in ranking:
    c += 1
    print(f'{c}ª Posição: {k} com {v}')
