import random
maquina = random.randint(0, 10)
soma = 0
ganhador = ''
par = ''
impar = ''
resultado = ''
c = 0
print('=-'*10, 'PAR OU IMPAR?', '=-'*10)
while True:
    jogador = int(input('Digite um valor: '))
    c += 1
    escolha = str(input('PAR ou ÍMPAR? ')).strip().upper()[0]
    while escolha not in 'PÍI':
        escolha = str(input('Opção inválida.\nPAR ou IMPAR?')).strip().upper()[0]
    print('-'*55)
    soma = jogador + maquina
    if soma % 2 == 0:
        resultado = 'PAR'
    else:
        resultado = 'IMPAR'
    print(f'Você jogou {jogador} e o computador {maquina}. Total de {soma} deu {resultado}.')
    print('-'*55)
    if escolha == par:
        maquina = impar
    else:
        maquina == par
    if escolha == resultado[0]:
        print('VOCÊ GANHOU.')
        print('=-'*30)
        break
    else:
        print('VOCÊ PERDEU.')
        print('=-'*30)
print(f'Você precisou de {c} rodada(s) para ganhar da máquina.')