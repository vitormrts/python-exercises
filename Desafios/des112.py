def voto(idade):
    if idade >= 18:
        return f'Com {idade} anos: voto OBRIGATÓRIO.'
    elif idade < 16:
        return f'Com {idade} anos: voto NEGADO.'
    elif 16 <= idade < 18:
        return f'Com {idade} anos: voto OPCIONAL.'


nasc = int(input('Ano de nascimento: '))
idade = 2020 - nasc
print(voto(idade))
