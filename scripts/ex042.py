"""Ecrever um programa que mostre se é um triÂnglo, e classifique em equilátero, isóceles e escaleno
"""

#Entrada de dados
lado_a = int(input('Digite o lado a: '))
lado_b = int(input('Digite o lado b: '))
lado_c = int(input('Digite o lado c: '))

"""Condições de um triângulo:
lado_a < lado_b + lado_c
lado_b < lado_a + lado_c
lado_c < lado_a + lado_b

"""
#Primeira Condição
if lado_a < lado_b + lado_c and lado_b < lado_a + lado_c and lado_c < lado_a + lado_b:
    print('Os segmentos acima, formam um triângulo!')
   #Classificação dos tringângulos
    if lado_a == lado_b == lado_c:
        print('EQUILÁTERO')
    elif lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
        print('ISÓCELES')
    else:
        print('ESCALENO')
else:
    print('Os segmentos acima, não formam um triângulo')
