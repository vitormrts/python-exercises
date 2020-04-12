import random
from time import sleep
print('='*90)
print('Vou pensar em um número de 0 a 5. Tente advinhar...')
print('='*90)
nadv = int(input('Em qual você pensou? '))
sleep(2)
print('PROCESSANDO...')
sleep(1)
print('.')
sleep(1)
print('.')
sleep(1)
print('.')
sleep(1)
num = random.randint(0, 5)
if nadv == num:
    print('DROGA! Você ganhou... Parabéns!')
else:
    print('HAHAHAHA! Eu ganhei! Boa tentativa.')