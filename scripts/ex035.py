"""Fazer um programa, que leia o comprimento de três retas e diga ao usuário se ela podem ou não construir um triângulo
"""

ladoa = float(input('Informe o lado A, do seu triângulo: '))
ladob = float(input('Informe o lado B, do seu triângulo: '))
ladoc = float(input('Informe o lado C, do seu triângulo: '))

"""Condição para um triângulo existir: 
b + c > ladoa > | b - c |
a + c > ladob > | a - c |
a + b > ladoc > | a - b |
"""

#Primeira condição
if (ladob + ladoc) > ladoa > abs(ladob - ladoc):
    print('É um triângulo!')
elif (ladoa + ladoc) > ladob > abs(ladoa - ladoc):
    print('É um triângulo!')
elif (ladoa + ladob) > ladoc > abs(ladoa - ladob):
    print('É um triângulo!')
else:
    print('Impossível ser um triângulo!')
