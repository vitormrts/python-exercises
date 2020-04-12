valor = int(input('Digite o valor que deseja sacar: '))
céd = 50
totcéd = 0
total = valor
while True:
    if total >= céd:
        total = total - céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'Total de {totcéd} de R${céd}.')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0
        if total == 0:
            break


