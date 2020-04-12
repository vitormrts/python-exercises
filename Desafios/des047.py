s1 = float(input('Digite o tamanho do primeiro segmento: '))
s2 = float(input('Digite o tamanho do segundo segmento: '))
s3 = float(input('Digite o tamanho do terceiro segmento: '))
if (s1 + s2) > s3 and (s2 + s3) > s1 and (s3 + s1) > s2:
    print('É possível fazer um triângulo', end=(' '))
    if s1 == s2 == s3:
        print('EQUILÁTERO.')
    elif s1 != s2 != s3 != s2:
        print('ESCALENO.')
    else:
        print('ISÓSCELES.')
else:
    print('Não é possível fazer um triângulo.')

