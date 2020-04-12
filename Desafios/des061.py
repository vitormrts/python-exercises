#lista = []
maiorpeso = 0
menorpeso = 0
for p in range(1,6):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(p)))
    if p == 1:
        maiorpeso = peso
        menorpeso = peso
    if peso > maiorpeso:
        maiorpeso = peso
    if peso < menorpeso:
        menorpeso = peso
    #lista += [peso]
    #maiorpeso = max(lista)
    #menorpeso = min(lista)
print(f'O maior peso é o de {maiorpeso}KG, já o menor peso é o de {menorpeso}KG.')