nome = input('Olá! Qual é o seu nome? ')
print(f'Prazer em te conhecer, {nome}!', end=' ')
n1 = float(input('Então, qual foi a nota de sua primeira prova? '))
n2 = float(input('Ok... E a nota da segunda avaliação? '))
m = n1+n2
mf = m/2
print(f'{nome}, a sua média final ficou avaliada em {mf}! Boa sorte.')