cont = 0
soma = 0
num = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    cont += 1
    soma += n
print('A soma dos {} números que você digitou, antes de escrever "999", é {}.'.format(cont, soma))
