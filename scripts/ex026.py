"""Faça um programa que leia uma frase pelo teclado e mostre:
a)quantas vezes aparece a letra 'A'
b)em que posição ela aparece pela primeira vez
c)em que posição ela aprece a última vez
"""
frase = str(input('Digie uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase'.format(frase.count('A')))
print('A primeira letra A aparece na posição {}'.format(frase.find('A')+1))
print('A últma letra A apareceu na posição {}'.format(frase.rfind('A')+1))
