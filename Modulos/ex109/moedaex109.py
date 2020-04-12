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
