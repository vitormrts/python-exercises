import math
ang = int(input('Digite um ângulo qualquer: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tg = math.tan(math.radians(ang))
print(f'O SENO de {ang} vale {sen:.2f}; \nO COSSENO de {ang} vale {cos:.2f}; \nA TANGENTE de {ang} vale {tg:.2f}.')

