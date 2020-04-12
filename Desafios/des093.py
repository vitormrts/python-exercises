# num1 = list()
num = list()
par = list()
impar = list()
for c in range(1, 8):
    num.append(int(input(f'Digite o {c}º valor: ')))
for n in num:
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
print('=-'*40)
par.sort()
impar.sort()
print(f'Os valores pares digitados foram {par}.'
      f'\nOs valores impares digitados foram {impar}.')