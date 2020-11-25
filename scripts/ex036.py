"""Escrever um programa para arovação de empréstimo imobiliário. O programa pergunta o valor do imóvel, o salário,
e em quantos anos ele vaipagar. Calcula o valor da parcela, que não pode ultrapassar 30% do salário do comprador
"""

valor_imovel = float(input('Digite o valor do imóvel que pretende comprar R$: '))
salario_mutuario = float(input('Digite o valor do seu salário R$:'))
prazo_emprestimo = float(input('Em quantos anos pretender financiar o imóvel: '))
valor_parcelas = valor_imovel / (prazo_emprestimo * 12)
minimo_parcela = salario_mutuario * 30 / 100
if valor_parcelas <= minimo_parcela:
    print('Empréstimo \033[1;36mAPROVADO\033[1m')
else:
    print('Empréstimo \033[1;31mNEGADO\033[m')
