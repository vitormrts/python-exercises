import random
n = 0
maquina = random.randint(0, 10)
c = 1
print('=-'*20, 'JOGO DE ADVINHAR', '=-'*20)
print('Olá! Será que você consegue advinhar em que número eu pensei de 1 a 10? ')
while n != maquina:
    n = int(input('Digite um valor: '))
    c += 1
    if n != maquina and n <= 10:
        print('Errou!')
    if n > 10:
        print('Cara... Eu pedi de 1 até 10.')
print('Você acertou na sua {}ª tentativa! '.format(c))