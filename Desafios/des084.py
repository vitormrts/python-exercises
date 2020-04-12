palavras = ('aprender', 'ensinar', 'programar', 'esforçar', 'amar', 'agradecer',
           'observar', 'descansar', 'brigar', 'ver', 'ler', 'viajar')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos', end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')

