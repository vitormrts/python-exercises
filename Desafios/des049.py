print('\033[1m='*20, '\033[1mLOJAS VITOR', '\033[1m=\033[m'*20)
compra = float(input('Preço das compras: \033[1;35mR$\033[m'))
print('FORMAS DE PAGAMENTO')
print('[ 1 ] à vista dinheiro/cheque')
print('[ 2 ] à vista cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')
opçao = int(input('Qual forma de pagamento você deseja? '))
if opçao == 1:
    preço = compra * 0.9
elif opçao == 2:
    preço = compra * 0.95
elif opçao == 3:
    preço = compra
else:
    preço = compra * 1.2
print('Sua compra de R${:.2f} custará R${:.2f} no final.'.format(compra, preço))