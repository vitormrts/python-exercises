sexo = str(input('Digite o seu sexo: [M/F] ')).upper().strip()[0]
while sexo not in 'FM':
    sexo = str(input('\033[1;31mOPÇÃO INVÁLIDA.\033[m\nDigite novamente: ')).upper().strip()[0]
print('\033[1mSexo {} registrado com sucesso'.format(sexo))