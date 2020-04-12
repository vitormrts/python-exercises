expressao = str(input('Digite a expressão: '))
lista = []
for simb in expressao:
    if simb == '(':
        lista.append('(')
    elif simb == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
     print('Sua expressão está válida.')
else:
    print('Sua expressãoe está errada. ')