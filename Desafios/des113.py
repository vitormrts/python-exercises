def fatorial(num, show=0):
    """
    -> Essa função calcula o fatorial de um determinado número.
    :param num: O número a ser calculado.
    :param show: Mostrar ou não a conta (True para mostrar, False para não).
    :return: O valor fatorial de um número num.
    """
    f = 1
    print(f'Calculando {num}! = ', end='')
    for c in range(num, 0, -1):
        f *= c
    if show == True:
        for c in range(num, 0, -1):
            print(c, end=' x ' if c > 1 else ' = ')
    return f


#Programa principal
n = int(input('Digite um valor: '))
print(fatorial(n, True))
