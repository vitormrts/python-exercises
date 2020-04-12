from time import sleep
def maior(*num):
    sleep(1)
    c = 0
    mai = 0
    print('=-'*30)
    print('Analisando os valores passados...')
    for n in num:
        print(n, end=' ', flush=True)
        sleep(0.3)
        c += 1
        if c == 1:
            mai = n
        else:
            if n > mai:
                mai = n
    sleep(0.5)
    print()
    print(f'Foram informados {c} números ao todo.')
    sleep(0.3)
    print(f'O maior valor informado foi {mai}')
    sleep(0.3)


maior(3, 9, 23, 13, 4, 6, 25, 43)
maior(3, 4, 1, 9, 4, 10, 12)
maior(1, 3, 2, 5)
maior(7, 9, 6, 2, 15)