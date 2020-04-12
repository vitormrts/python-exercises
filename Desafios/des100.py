from datetime import date
dados = dict()
dados['Nome'] = str(input('Nome: '))
dados['Ano de Nascimento'] = int(input('Ano de Nascimento: '))
dados['CTPS'] = int(input('Carteira de Trabalho (0 se não tem): '))
idade = date.today().year - dados['Ano de Nascimento']
dados['Idade'] = idade
if dados['CTPS'] != 0:
    dados['Ano de Contratação'] = int(input('Ano de Contratação: '))
    dados['Salário'] = float(input('Salário: R$'))
    valor = date.today().year - dados['Ano de Contratação']
    aposentar1 = 35 - valor
    aposentar2 = aposentar1 + idade
    dados['Aposentadoria'] = aposentar2

for k, v in dados.items():
    print(f'{k} tem o valor {v}')
