n1 = float(input('Digite a sua primeira nota: '))
n2 = float(input('Digite a sua segunda nota: '))
media = (n1+n2)/2
print('Sua média ficou avaliada em {:.1f}.'.format(media))
if media < 5:
    print('O aluno está REPROVADO.')
elif media >= 5 and media < 7:
    n3 = 21 - n1 - n2
    print('O aluno está de RECUPERAÇÃO. Portanto, precisa tirar {} para ser aprovado. '.format(n3))
else:
    print('O aluno está APROVADO.')