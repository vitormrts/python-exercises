nome = input('\033[1;31mOlá! Qual é o seu nome? ')
n1 = int(input(f'\033[1;31mMuito prazer, {nome}!\n\033[34mPor favor, poderia digitar um número? '))
n2 = int(input('\033[34mCerto! Digite outro número: '))
print('\033[32mHm... Deixe-me pensar...\033[m')
s = n1+n2
print('.')
print('.')
print('.')
print('.')
print('.')
print('.')
print(f'\033[33mJá sei!!! A soma de \033[1;35m{n1}\033[m e \033[1;36m{n2}\033[m é \033[1;31m{s}\033[m! Correto? ')