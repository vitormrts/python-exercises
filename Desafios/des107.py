from time import sleep
def contador(i, f, r):
    print('='*30)
    print(f'Contador de {i} até {f} de {r} em {r}')
    sleep(0.3)
    c = i
    if i < f:
        while c <= f:
            print(c, end=' ')
            c += r
            sleep(0.3)
        print()
    elif i > f:
        while c >= f:
            print(c, end=' ')
            c -= r
            sleep(0.3)
        print()
    sleep(0.3)


contador(1, 10, 1)
contador(10, 0, 2)
i = int(input('Agora é a sua vez.\nInício: '))
f = int(input('Fim: '))
r = int(input('Razão: '))
contador(i, f, r)