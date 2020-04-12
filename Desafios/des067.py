a1 = int(input('Digite o valor do primeiro termo da P.A: '))
r = int(input('Digite a razão da P.A: '))
termo = a1
cont = 1
mais = 0
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{}'.format(termo), end=' -> ')
        termo = termo + r
        cont = cont + 1
    print('PAUSA')
    mais = int(input('\nQuantos termos você deseja adicionar? '))
print('Finalizando...')


