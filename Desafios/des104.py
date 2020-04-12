jogador = int(input('Deseja multiplicar os valores por qual valor? '))
def escolha(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= jogador
        pos += 1


numeros = [3, 4, 1]
print(f'Os numeros {numeros} multiplicados por {jogador} são ', end='')
escolha(numeros)
print(numeros)


