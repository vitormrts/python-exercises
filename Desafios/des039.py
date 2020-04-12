r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))
reta1 = r1+r2
reta2 = r2+r3
reta3 = r1+r3
if reta1 > r3 and reta2 >r1 and reta3 > r2:
    print('É possível fazer um triângulo.')
else:
    print('Não é possível fazer um triângulo.')