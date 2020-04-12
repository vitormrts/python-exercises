from random import randint
from time import sleep
print('='*20)
print('     MEGA-SENA     ')
print('='*20)
lista = [randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60)]
escolha = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'  SORTEANDO {escolha} JOGOS    ')
for c in range(0, escolha):
    print(f'Jogo {c+1}: {lista}')
    sleep(0.5)
print('='*20)
print('     BOA SORTE!')


