frase = str(input('Digite uma frase: ')).lower()
print('Sobre a letra "a": \nQuantas vezes ela aparece? {} vezes;'.format(frase.count('a')))
print('Em que posição ela aparece pela primeira vez? {};'.format(frase.strip().index('a')+1))
print('Em que posição ela aparece pela última vez? {}.'.format(frase.strip().rfind('a')+1))
