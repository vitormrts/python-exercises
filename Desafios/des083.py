listagem = ('Notebook', 1499.99,
            'Celular', 999.90,
            'PC Gamer', 3199.00,
            'Playstation 4', 999.90,
            'Cadeira XRacer', 690.00,
            'Fone de ouvido', 49.90,
            'Headset', 99.90,
            'Mouse', 29.90)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<40}', end='')
    else:
        print(f'R${listagem[pos]:>8}')
