from time import sleep


#Cores
cores = ['\033[7;34;40m',   #0 = Azul
         '\033[7;33;40m',   #1 = Amarelo
         '\033[7;32;40m',   #2 = Verde
         '\033[7;31;40m',   #3 = Vermelho
         '\033[7;35;40m',   #4 = Magenta
         '\033[m']          #5 = Sem cor

#Linhas
def linhas(txt):
    tam = '=' * (len(txt) + 4)
    print(f'{cores[0]}{tam}')
    print(f'  {cores[0]}{txt}  ')
    print(f'{cores[0]}{tam}')


#Pausa
def pausa(msg=0):
    for c in range(0, 3):
        sleep(1)
        print(f'{cores[2]}.')
    return msg

#Escolha
def escolha(msg):
    while True:
        linhas('SISTEMA DE AJUDA PyHELP')
        direcionamento = str(input(msg)).lower()
        if direcionamento == 'fim':
            break
        if direcionamento.isalpha():
            linhas(f'Acessando o manual do comando {direcionamento}...')
            pausa()
            sleep(1)
            print(f'{cores[4]}')
            help(direcionamento)
        else:
            print(f'{cores[3]}ERRO! Escolha uma função/biblioteca válida. ')
    linhas(f'Até logo!')


#Programa principal
direcionamento = escolha(f'{cores[5]}Função ou biblioteca > ')
