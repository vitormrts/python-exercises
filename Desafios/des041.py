from time import sleep
print('\033[1;30m='*35)
print('\033[1;31mCALCULO DE EMPRÉSTIMO BANCÁRIO')
print('\033[1;30m='*35)
sleep(1)
print('\033[1m.')
sleep(1)
print('\033[1m.')
sleep(1)
print('\033[1m.')
sleep(1)
casa = float(input(('\033[34mQual é o valor da casa que deseja comprar? \033[1;32mR$')))
sleep(1)
anos = float(input(('\033[34mEm quantos anos você pretende comprá-la? ')))
sleep(1)
salario = float(input(('\033[34mQual é o valor de seu salário? \033[1;32mR$')))
sleep(0.5)
print('\033[1;31mPROCESSANDO...')
sleep(1)
print('\033[1m.')
sleep(1)
print('\033[1m.')
sleep(1)
print('\033[1m.')
sleep(0.5)
meses = anos*12
mensalidade = casa/meses
print(f'\033[33mPara pagar uma casa de R${casa:.2f} em {anos:.0f} anos, a prestação mensal será de R${mensalidade:.2f}.')
if mensalidade < 0.3 * salario:
    print('\033[mEmpréstimo \033[1;32mAPROVADO\033[m!')
else:
    print('\033[mEmpréstimo \033[1;31mNEGADO\033[m!')
