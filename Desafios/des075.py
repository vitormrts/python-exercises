print('=-'*20)
print('MERCADINHO BIG-BOOM')
print(('=-'*20))
soma = 0
produto = 0
cont1000 = 0
produtomenorpreço = 0
nomeprodutomenor = ''
while True:
    produto += 1
    nome = str(input('Nome do Produto: ')).strip().title()
    preço = int(input('Preço: R$'))
    soma += preço
    if preço > 1000:
        cont1000 += 1
    if produto == 1:
        menorpreço = preço
        nomeprodutomenor = nome
    elif produto > 1:
        if preço < menorpreço:
            menorpreço = preço
            nomeprodutomenor = nome

    continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('\033[1;31mOPÇÃO INVÁLIDA\033[m\nQuer continuar? [S/N]')).strip().upper()[0]
    if continuar == 'N':
        break
print('=-'*20)
print('FIM DO PROGRAMA')
print('=-'*20)
print(f'O total da compra foi R${soma}\n'
      f'Temos {cont1000} produtos que custam mais de R$1000.00'
      f'\nO produto mais barato foi {nomeprodutomenor} que custou R${menorpreço}.')



