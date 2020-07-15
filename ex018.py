""" Leia um ângulo qualquer e mostre na tela, seno, cosseno e tangente
"""
from math import sin, cos, tan, radians
angulo = float(input('Digite um ângulo: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians((angulo)))
print('O ângulo de {} tem o SENO de {:.2}: '.format(angulo, seno))
print('O ângulo de {} tem o COSSENO de {:.2}: '.format(angulo, cosseno))
print('O ângulo de {} tem a TANGENTE de {:.2}: '.format(angulo, tangente))
