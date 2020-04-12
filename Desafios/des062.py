idadetotal = 0
idademedia = 0
contadormulher = 0
homemvelho = 0
lista = []
nomevelho = ''
for p in range(1, 5):
    print('=-'*20, f'{p}ª PESSOA', '=-'*20)
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('M/F: '))
    idadetotal += idade
    idademedia = idadetotal/4
    if sexo in 'Ff':
        if idade < 20:
            contadormulher += 1
    if sexo in 'Mm':
        if p == 1:
            homemvelho = idade
            nomevelho = nome
        if idade > homemvelho:
            homemvelho = idade
            nomevelho = nome
print(f'A média de idade do grupo é de {idademedia:.0f} anos.\nAlém disso, há, no total, {contadormulher} mulhere(s) com menos de 20 anos.')
print(f'O homem mais velho tem {homemvelho} anos, e seu nome é {nomevelho}.')
