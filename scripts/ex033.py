"""Faça um programa que leia três núemeros e mostre qual é o maior e qual é o menor"""

a1 = int (input('Digite o primeiro valor: '))
a2 = int (input('Digite o segundo valor: '))
a3 = int (input('Digite o terceiro valor: '))
#Verificando o menor valor
menor = a1
if a2 < a1 and a2 < a3:
    menor = a2
if a3 < a1 and a3 < a2:
    menor = a3
#Verificando quem é o maior
maior = a1
if a2 > a1 and a2 > a3:
    maior = a2
if a3 > a1 and a3 > a2:
    maior = a3
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))

