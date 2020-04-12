n = int(input('Escolha um número de 0 a 20: '))
while n < 0 or n > 20:
    n = int(input('Opção Inválida.\nEscolha um número de 0 a 20: '))
numerosnome = ('um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesste', 'dezoito', 'dezenove', 'vinte')
print(f'Você digitou o número {numerosnome[n-1]}.')