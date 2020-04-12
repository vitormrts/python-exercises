def aumentar(p, taxa):
    res = p * (1 + taxa/100)
    return res


def diminuir(p, taxa):
    res = p * (1 - taxa/100)
    return res


def dobro(p):
    res = p * 2
    return res


def metade(p):
    res = p / 2
    return res