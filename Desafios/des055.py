soma = 0
contador = 0
contador2 = 0
for c in range(1, 7):
    num = int(input('Digite um valor: ')) #Valor
    contador2 = contador2 + 1
    if num % 2 == 0:
        soma = soma + num
        contador = contador + 1
print('A soma de todos os {} números pares entre os {} valores é {}.'.format(contador, contador2, soma))
