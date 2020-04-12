num = int(input('Digite um número qualquer: '))
base = int(input('Qual base de conversão você deseja? \n[ 1 ] converter para BINÁRIO\n[ 2 ] Converter para OCTAL\n[ 3 ] Converter para HEXADECIMAL\nSua opção: '))
if base == 1:
    print('{} para BINÁRIO é {}'.format(num, bin(num)[2:]))
elif base == 2:
    print('{} para HEXAL é {}'.format(num, oct(num)[2:]))
elif base == 3:
    print('{} para HEXADECIMAL é {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida. Tente novamente.')