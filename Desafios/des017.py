dia = float(input('Quantos dias você utilizou carro alugado? '))
km = float(input('Quantos quilômetros você rodou com ele? '))
p1 = 60 * dia
p2 = (15/100) * km
pt = p1 + p2
print(f'Você deverá pagar R${pt:.2f}.')