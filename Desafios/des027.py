nome = str(input('Digite o nome de uma cidade: '))
separada = nome.split()
pgt = 'Santo' in separada[0]
print('{} começa com o nome Santo? {} '.format(nome, pgt))
