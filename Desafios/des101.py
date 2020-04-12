dados = dict()
temp = []
princ = []
gols = list()
c = 0
c2 = 0
c3 = 0
total = 0
while True:
    total = 0
    dados['Nome'] = str(input('Nome do Jogador: ')).capitalize().strip()
    partidas = int(input(f'Quantas partidas {dados["Nome"]} jogou? '))
    for c in range(1, partidas+1):
        gols.append(int(input(f'Quantos gols na partida {c}? ')))
        dados['gols'] = gols[:]
    for g in gols:
        total += g
        dados['total de gols'] = total
    princ.append(dados.copy())
    gols.clear()
    del total
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
print('=-'*40)
print('No. ', end='')
for k in dados.keys():
    print(f'{k:<15}', end='')
print()
print('=-'*40)
for k, v in enumerate(princ):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('=-'*40)
jog = int(input('Mostrar dados de qual jogador (999 para parar)? '))
while True:
    if jog <= len(princ):
        print(f'LEVANTAMENTO DO JOGADOR {princ[jog]["Nome"]}')
        # c = 0
        # print(f'O jogador {dados["Nome"]} fez {partidas} partidas, sendo que: ')
        # for c in range(1, partidas+1):
        #     print(f'Na {c}ª partida, fez {dados["gols"][c-1]}')
        #     print(f'Foi um total de {total} gols.')
    elif jog == 999:
        break
    else:
        jog = int(input(f'ERRO! Não existe jogador com o No. {jog}\nMostrar dados de qual jogador (999 para parar)?'))