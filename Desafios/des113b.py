def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um número
    :param n: o número a ser calculado
    :param show: mostrar ou nao a conta
    :return: retorna o fatorial de um numero n
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end=' x ' if c > 1 else ' = ')
        f *= c
    return f


print(fatorial(5, True))
help(fatorial)