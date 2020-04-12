cont = 0
while True:
    print('=-'*40)
    n = int(input('Quer ver a tabuada de qual valor? (Digite um número negativo para parar) '))
    print('=-'*40)
    if n >= 0:
        for c in range(0, 11):
            print(f'{n} x {c:2} = {n * c}')
    #print('=-'*40)
        #while cont < 10:
            #cont += 1
            #print(f'{n} x {cont} = {n * cont}')
    if n < 0:
        break
print('TABUADA ENCERRADA!')
