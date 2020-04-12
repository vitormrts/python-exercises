tabelabr = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico-PR', 'São Paulo', 'Internacional', 'Corinthians', 'Fortaleza', 'Goiás', 'Bahia', 'Vasco', 'Atlético-MG', 'Fluminense', 'Botafogo', 'Ceará', 'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí')
print('='*40, '\nTABELA BRASILEIRÃO 2020 SÉRIE A')
print('='*40)
print('Os 5 primeiros colocados são: ')
cont = 0
cont2 = 15
for c in range(0, 5):
    cont += 1
    print(f'{cont}º {tabelabr[cont - 1]}')
print(f'='*40)
print('Os 4 últimos colocados são: ')
for c in range(16, 20):
    cont2 += 1
    print(f'{cont2 + 1}º {tabelabr[cont2]}')
print(f'='*40)
print(f'Times em ordem alfabética: {sorted(tabelabr)}')
print('='*40)
print('A Chapecoense está na {} posição.'.format(tabelabr.index('Chapecoense')+1))