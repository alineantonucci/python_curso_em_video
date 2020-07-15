""" Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, 
e calcule a hipotenusa
"""

cateto_adjacente = float(input('Digite o cateto adjacente: '))
cateto_oposto = float(input('Digite cateto oposto: '))
catetos = (cateto_adjacente ** 2) + (cateto_oposto ** 2)
hipotenusa = (catetos)**(1/2)
print('A hipotenusa é: {:.2f}'
      .format(hipotenusa))
