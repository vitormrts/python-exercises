num = [[], []]
for c in range(0, 7):
    valor = int(input('Digite um valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
num[0].sort(reverse=True)
num[1].sort(reverse=True)
print(f'ÍMPARES: {num[1]}')
print(f'PARES: {num[0]}')