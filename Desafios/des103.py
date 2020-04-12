temp = []
princ = []
def contador(* num):
    soma = 0
    tam = len(num)
    print(f'Recebi os valores {num}, que ao todo são {tam}. Os valores pares são ', end='')
    for n in num:
        if n % 2 == 0:
            temp.append(n)
    princ.append(temp[:])
    for pares in princ:
        for p in pares:
            print(p, end=' ')
            soma += p
    print(f'e a soma é {soma}')
    princ.clear()
    temp.clear()

contador(5, 4, 3, 2)
contador(4, 2, 1, 6, 7, 8, 2)
# for pares in princ:
#     for p in pares:
#         print(p, end=' ')
#     print()
