temp = list()
princ = list()
while True:
    temp.append(str(input('Nome: ')))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    nm = (n1+n2)/2
    temp.append(nm)
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'{"No.":<4}{"Nome":<10}{"Média":>8}')
for pos, dado in enumerate(princ):
    print(f'{pos:<4}{dado[0]:<10}{dado[1]:>8}')