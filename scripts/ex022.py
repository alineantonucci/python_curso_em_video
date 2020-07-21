""" Programa lê o nome completo de uma pessoa e mostra:
a)nome com todas letras maísculas e minúsculas
b) quantas letras no total sem espaço
c) quantas letras primeiro nome
"""

nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em letras maiúculas é {}'.format(nome.upper( )))
print('Seu nome em letras minúsculas é {}'.format(nome.lower( )))
print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
