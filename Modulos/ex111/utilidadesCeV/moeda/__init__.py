def moeda(funcao, moeda='R$'):
    return f'{moeda}{funcao:.2f}'.replace('.', ',')


def aumentar(p, taxa, mostrar=False):
    res = p * (1 + taxa/100)
    return res if mostrar is False else moeda(res)


def diminuir(p, taxa, mostrar=False):
    res = p * (1 - taxa/100)
    return res if mostrar is False else moeda(res)


def dobro(p, mostrar=False):
    res = p * 2
    return res if mostrar is False else moeda(res)


def metade(p, mostrar=False):
    res = p / 2
    return res if mostrar is False else moeda(res)


def resumo(p=500, aumento=0, desconto=0):
    print('='*30)
    print('        LOJÃO BARATÃO    ')
    print('='*30)
    print(f'{"Preço analisado:":<20}{moeda(p):<10}' 
           f'\n{"Dobro do preço:":<20}{dobro(p, True):<10}' 
           f'\n{"Metade do preço:":<20}{metade(p, True):<10}' 
           f'\n{aumento:<2}{"% de aumento:":<18}{aumentar(p, aumento, True):<10}' 
           f'\n{desconto:<2}{"% de desconto:":<18}{diminuir(p, desconto, True):<10}' 
           f'\n{"="*30}')