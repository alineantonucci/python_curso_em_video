"""Fazer um programa que calcula o aumento de salário de acordo com a faixa salarial"""

salario = float (input('Informar o salário do funcionário: '))
if salario <= 1250 :
    novo = salario + (1.15)
else:
    novo = salario + (1.10)
print('Quem ganhava R$ {:.2f}, passará a ganhar R$ {:.2f}'.format(salario,novo))
