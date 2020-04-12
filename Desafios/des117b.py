from time import sleep

#Cores
cores = ['\033[7;34;40m',   #0 = Azul
         '\033[7;33;40m',   #1 = Amarelo
         '\033[7;32;40m',   #2 = Verde
         '\033[7;31;40m',   #3 = Vermelho
         '\033[7;35;40m',   #4 = Magenta
         '\033[m']          #5 = Sem cor


def ajuda(com):
    titulo(f'Acessando o manual do comando {comando}...', 1)
    for c in range(0, 3):
        print(cores[1])
        sleep(1)
        print('.')
    sleep(1)
    print(cores[5])
    print(cores[4], end='')
    help(comando)
    print(cores[5])


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(cores[cor], end='')
    print('='*tam)
    print(f'  {msg}  ')
    print('='*tam)
    print(cores[5], end='')


# Programa Principal
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHelp', 3)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        titulo('ATÉ LOGO!', 2)
        break
    else:
        ajuda(comando)
