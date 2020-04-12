dados = dict()
pessoas = list()
f = []
c = 0
tot = 0
media = 0
mai = []
while True:
    c += 1
    dados['Nome'] = str(input('Nome: ')).strip().capitalize()
    dados['Idade'] = int(input('Idade: '))
    tot += dados['Idade']
    dados['Sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
    pessoas.append(dados.copy())
    if dados['Sexo'] == 'F':
        f.append(dados['Nome'])
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    media = tot / c
    if resp == 'N':
        break
print(f'Foram cadastradas {c} pessoas.')
print(f'A média de idade é de {media:.0f} anos.')
print(f'O nome das mulheres é ', end='')
for n in f:
    print(n, end=' ')
for p in pessoas:
    if p['Idade'] >= media:
        for k, v in p.items():
            print(f'\n{k} = {v}; ')
