import random
from time import sleep
print('='*20, 'JOKENPÔ', '='*20)
jogadas = ('Pedra', 'Papel', 'Tesoura')
#maquina = random.randint(0, 2)
maquina = random.choice(jogadas)
print("""Vamos brincar de JOKENPÔ?'
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA""")
jogador = int(input('Escolha a sua jogada: '))
sleep(1)
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PÔ !!!')
sleep(1)
print('PROCESSANDO...')
sleep(1)
print('='*40)
print('Computador jogou {}\nJogador jogou {}'.format(maquina, jogadas[jogador - 1]))
print('='*40)
if jogador == 1 and maquina == 0 or jogador == 2 and maquina == 1 or jogador == 3 and maquina == 2:
    jogo = 'EMPATE!!!'
elif jogador == 1 and maquina == 2 or jogador == 2 and maquina == 0 or jogador == 3 and maquina == 1:
    jogo = 'Vitória do JOGADOR!!!'
else:
    jogo = 'Vitória do COMPUTADOR!!!'
print(jogo)