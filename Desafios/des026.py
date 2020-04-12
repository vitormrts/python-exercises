num = int(input('Digite um número de 0 a 9999: '))
u = num // 1 % 10
d = ((num % 100) - u)/10
c = ((num % 1000) - (u + (d*10)))/100
m = ((num % 10000) - ((u*10) + (d*100))) /1000
print('Unidade: {}'.format(u))
print('Dezena: {:.0f}'.format(d))
print('Centena: {:.0f}'.format(c))
print('Milhar: {:.0f}'.format(m))