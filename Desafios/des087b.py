numeros = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso. ')
    else:
        print('Valor duplicado! Não adicionarei.')
    resposta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resposta == 'N':
        break
print('='*30)
print(f'Você digitou os valores {numeros}')