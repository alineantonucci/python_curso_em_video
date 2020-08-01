"""Escreva um número de 0 a 5 e peça para o usuário tentar descobrir qual foi o número escolhido.
O programa deverá escrever na tela se o usuário vendeu ou perdeu
"""
from random import randint

nome = str(input('Digite o seu nome: '))
print('Olá {}, vamos jogar? '.format(nome))
numero_sorteio = int(input('Digite um número inteiro de 0 a 5: '))
numero_aleatorio = randint(0, 5) # Sorteia um número aleatório
if numero_sorteio == numero_aleatorio:
    print('Parabéns, você VENCEU!')
else:
    print('Você PERDEU')
print('---FIM---')