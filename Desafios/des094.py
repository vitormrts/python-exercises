linhas = [[], [], []]
valores = []
par = 0
c3 = 0
maior = 0
c = 0
for c in range(0, 3):
    valor = int(input(f'Digite um valor para [0, {c}]: '))
    linhas[0].append(valor)
    valores += [valor]
for c in range(0, 3):
    valor = int(input(f'Digite um valor para [1, {c}]: '))
    linhas[1].append(valor)
    valores += [valor]
for c in range(0, 3):
    valor = int(input(f'Digite um valor para [2, {c}]: '))
    linhas[2].append(valor)
    valores += [valor]
for v in valores:
    if v % 2 == 0:
        par += v
c3 = linhas[0][2] + linhas[1][2] + linhas[2][2]
print('=-'*30)
print(f'[ {linhas[0][0]} ] [ {linhas[0][1]} ] [ {linhas[0][2]} ]')
print(f'[ {linhas[1][0]} ] [ {linhas[1][1]} ] [ {linhas[1][2]} ]')
print(f'[ {linhas[2][0]} ] [ {linhas[2][1]} ] [ {linhas[2][2]} ]')
print('=-'*30)
print(f'A soma dos valores pares é {par}.'
      f'\nA soma dos valores da terceira coluna é {c3}.'
      f'\nO maior valor da segunda linha é {max(linhas[1])}.')