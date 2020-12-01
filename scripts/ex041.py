"""Programa para categorizar os atletas de acordo com a idade
"""
#Entrada de valores
nasc_atleta = int(input('Digite seu ano de nascimento: '))
from datetime import datetime
hoje = datetime.today().year
#calculo da idade do atleta
idade_atleta = hoje - nasc_atleta
print('O atleta tem {} anos.'.format(idade_atleta))
#classificação dos atletas de acordo com idade
if idade_atleta <= 9:
    print('Atleta MIRIM')
elif idade_atleta <= 14:
    print('Atleta INFANTIL')
elif idade_atleta <= 19:
    print('Atleta JUNIOR')
elif idade_atleta <= 20:
    print('Atleta SENIOR')
else:
    print('Atleta MASTER')
