a1 = int(input('Digite o valor do primeiro termo da P.A: '))
r = int(input('Digite a razão da P.A: '))
#a10 = a1 + (10-1)*r
for c in range(a1, 10, r):
    print(c, end=' → ')
print('ACABOU.')