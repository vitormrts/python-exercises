while True:
    def leiaint(n):
        global num
        global pgt
        leiaint = input(n)
        num = leiaint
        pgt = num.isnumeric()
        return leiaint

    num = 0
    pgt = False

    escolha = leiaint('Digite um número: ')
    if pgt:
        break
    else:
        print('\033[1;31mOPÇÃO INVÁLIDA.\033[m')
print(f'Você digitou o número {num}')