def notas(* num, sit=False):
    """
    -> Função para analisar as notas dos alunos de uma sala.
    :param num: uma ou mais notas de alunos de uma determinada sala
    :param sit: opcional, mostra se a sala está abaixo, na média, ou acima da média.
    :return: dicionário com várias informações sobre a situação da turma
    """
    dados = dict()
    soma = 0
    c = 0
    for n in num:
        c += 1
        soma += n
    qntd = c
    mai = 0
    men = 0
    c1 = 0
    for n in num:
        c1 += 1
        if c1 == 1:
            mai = num[c1-1]
            men = num[c1-1]
        else:
            if num[c1-1] > mai:
                mai = num[c1-1]
            if num[c1-1] < men:
                men = num[c1-1]
    dados['quantidade de notas'] = c
    dados['media'] = soma/c
    dados['maior'] = mai
    dados['menor'] = men
    if sit == True:
        if soma/c < 5:
            print(f'A sala está ABAIXO da média.')
        elif 5 <= soma/c <= 8:
            print(f'A sala está na média.')
        else:
            print(f'A sala está ACIMA da média.')
    print(dados)
    return dados


resp = notas(1, 9, 5, 2, sit=True)