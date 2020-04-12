#0, 1, 1, 2, 3, 5, 8...
termostotais = int(input('Quantos termos você quer mostrar? '))
#fibonacci = termoatual - termoanterior
cont = 3
t1 = 0
t2 = 1
print('{} -> {}'.format(t1, t2), end=' -> ')
while cont <= termostotais:
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    cont += 1
    print(t3, end=' -> ')
print('FIM')

#t3 = t1 + t2


