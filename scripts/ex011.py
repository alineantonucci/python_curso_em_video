""" Faça um programa que leia a largura e a altura de uma parede em metros, calcule
a sua área e a quantidade de tinta necessária para pintá-la, sabendo que 1l de tinta,
pinta uma área de 2 m2.
"""

l = float(input('Digite a largura da parede em metros: '))
a = float(input('Digite a altura da parede em metros: '))
print('Sua parede tem a dimensão de {}m x {}m e sua área é igual a: {} m2.'.format(l,a,l*a))
print('Para pintar essa parede, você precisará de {} litros de tinta.'.format((l*a)/2))
