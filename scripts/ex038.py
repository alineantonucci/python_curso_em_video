"""Ecreva um programa que leia dois numeros inteiros e compare-os, mostrando na tela quem é maior, menor ou se são
iguais
"""

numero1 = int(input('Digite um número inteiro: '))
numero2 = int(input('Digite outro número inteiro: '))
if numero1 > numero2:
    print('O primeiro valor é  MAIOR')
elif numero1 < numero2:
    print('O primeiro valor é MENOR')
else:
    print('Não existe valor maior, os dois vaor são IGUAIS')
