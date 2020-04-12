from moeda import moedaex107


preco = float(input('Valor do produto: R$'))
print(f'Aumentando 10%, o preço é de {moedaex107.aumentar(preco, 10)}')
print(f'Diminuindo 10%, o preço é de {moedaex107.diminuir(preco, 10)}')
print(f'O preço pela metade é de {moedaex107.metade(preco)}')
print(f'O dobro do preço é de {moedaex107.dobro(preco)}')