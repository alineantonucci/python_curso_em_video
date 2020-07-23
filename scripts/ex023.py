"""Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados
"""

numero_1 = int(input('Digite um número: '))
numero_2 = str(numero_1)
print('Analisando o número {}'.format(numero_1))
print('Unidade {}'.format(numero_2[3]))
print('Dezena {}'.format(numero_2[2]))
print('Centena {}'.format(numero_2[1]))
print('Milhar {}'.format(numero_2[0]))
