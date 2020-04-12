a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))
#Quem é o maior
if a>b and a>c:
    maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
#Quem é o menor
if a<b and a<c:
    menor = a
if b<a and b<c:
    menor = b
if c<b and c<a:
    menor = c
#Resultado
print('O maior valor é {}. \nO menor valor é {}.'.format(maior, menor))



