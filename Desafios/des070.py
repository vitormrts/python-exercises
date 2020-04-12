continuar = ''
cont = 0
soma = 0
media = 0
lista = []
while continuar in 'Ss':
    num = int(input('Digite um número: '))
    continuar = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    while continuar not in 'SsNn':
        continuar = str(input('Opção inválida.\n Deseja continuar [S/N]?')).strip().upper()[0]
    cont += 1
    soma += num
    media = soma/cont
    #if num = 1:
    lista += [num]
print('A média entre os {} números escolhidos é {:.1f}.\n'.format(cont, media))
print('Além disso, o maior número digitado é {} e o menor número é {}.'.format(max(lista), min(lista)))