pessoa = dict()
dados = []
pessoa['Nome'] = str(input('Nome: '))
pessoa['Nota'] = float(input(f'Média de {pessoa["Nome"]}: '))
if pessoa['Nota'] >= 5:
    pessoa['Situação'] = 'Aprovado'
else:
    pessoa['Situação'] = 'Reprovado'
dados.append(pessoa.copy())
for p in dados:
    for k, v in p.items():
        print(f'{k} é igual a {v}')

