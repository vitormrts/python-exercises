def area(h, l):
    area = h * l
    print(f'A área de um terreno {h} x {l} é de {area}m²')


print('=-' * 20)
print('           CÁLCULO DE ÁREA            ')
print('=-' * 20)
h = float(input('Altura (m): '))
l = float(input('Largura (m): '))
area(h, l)

