valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resposta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resposta in 'N':
        break
print(f'Você digitou {len(valores)}.')
valores.sort(reverse=True)
print(f'A ordem decrescente é {valores}')
if 5 in valores :
    print('O valor 5 faz parte da lista. ')
else:
    print('O valor 5 não foi encontrado na lista. ')