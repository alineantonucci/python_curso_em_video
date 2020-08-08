"""Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO
"""

from datetime import date
ano_analisado = int(input('Digite o ano que você quer analisar? Coloque 0 para analisar o ano atual: '))
if ano_analisado == 0:
    ano_analisado = date.today().year
if ano_analisado % 4 == 0 and ano_analisado % 100 !=0 or ano_analisado % 400 ==0:
    print(' {} é um ano  BISSEXTO'.format(ano_analisado))
else:
    print('{} não é um ano BISSEXTO'.format(ano_analisado))
print('FIM')
