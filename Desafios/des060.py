from datetime import date
hoje = date.today().year
contadormaior = 0
contadormenor = 0
for p in range(1, 8):
    nasc = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(p)))
    idade = hoje - nasc
    if idade >= 18:
        contadormaior += 1
    else:
        contadormenor +=1
print(f'Há {contadormaior} pessoas maiores de idade e {contadormenor} pessoas menores de idade.')
