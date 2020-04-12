dados = list()
galera = list()
cp = 0
c = 0
maior = 0
menor = 0
nomemaior = list()
nomemenor = list()
while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))
    galera.append(dados[:])
    cp += 1
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp in 'N':
        break
    dados.clear()
for p in galera:
    c += 1
    if c == 1:
        maior = p[1]
        menor = p[1]
        nomemaior.append(p[0])
        nomemenor.append(p[0])
    else:
        if p[1] > maior:
            maior = p[1]
            nomemaior.pop()
            nomemaior.append(p[0])
        elif p[1] < menor:
            menor = p[1]
            nomemenor.pop()
            nomemenor.append(p[0])
        elif p[1] == maior:
            nomemaior.append(p[0])
        elif p[1] == menor:
            nomemenor.append(p[0])
print(f'Ao todo, {cp} pessoas foram cadastradas.')
print(f'\nO maior peso foi de {maior}Kg. Peso de {nomemaior}'
      f'\nO menor peso foi de {menor}Kg. Peso de {nomemenor}')