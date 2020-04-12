import moeda


preco = float(input('Valor do produto: R$'))
print(f'Aumentando 10%, o preço é de {moeda.aumentar(preco, 10, True)}')
print(f'Diminuindo 10%, o preço é de {moeda.diminuir(preco, 10, True)}')
print(f'O preço pela metade é de {moeda.metade(preco, True)}')
print(f'O dobro do preço é de {moeda.dobro(preco, True)}')