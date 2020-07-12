""" Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares e Euros
ela pode comprar.

Considere U$$ 1,00 = R$ 3,27
"""

real = float(input("Quanto dinheiro você na carteira? R$ "))
print('Com R$ {:.2f}, você pode comprar U$ {:.2f}.'.format(real, real/3.27))
print('Com R$ {:.2f}, você pode comprar {:.2f} Euros.'.format(real, real/6.03))

