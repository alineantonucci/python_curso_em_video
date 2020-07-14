"""Crie um programa que leia um número real qualquer pelo teclado e mostre na tela sua porção inteira
"""

from math import trunc
num = float(input('Digite um número real qualquer: '))
print('O número arrendondao é igual: {}.'
      .format(trunc(num)))

