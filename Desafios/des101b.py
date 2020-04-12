time = []
jogador = dict()
partidas = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: ')).capitalize().strip()
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'Quantos gols na partida {c}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if resp in 'SN':
            break
        else:
            print(f'ERRO! Responda apenas [S/N]')
    if resp == 'N':
        break
print('-'*40)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15} ', end='')
print()
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15} ', end=' ')
    print()
print('-'*30)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    elif busca >= len(time):
        print(f'ERRO. Não existe o jogador com código {busca}. ')
    else:
        print(f'  LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}')
        for i, g in enumerate(time[busca]['gols']):
            print(f'     Na partida {i}, {time[busca]["nome"]} fez {g} gols.')
