import moeda


preco = float(input('Valor do produto: R$'))
print(f'Aumentando 10%, o preço é de {moeda.moeda(moeda.aumentar(preco, 10))}')
print(f'Diminuindo 10%, o preço é de {moeda.moeda(moeda.diminuir(preco, 10))}')
print(f'O preço pela metade é de {moeda.moeda(moeda.metade(preco))}')
print(f'O dobro do preço é de {moeda.moeda(moeda.dobro(preco))}')