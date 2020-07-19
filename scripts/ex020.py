"""Ler o nome dos alunos, e sortear a ordem de apresentação de trabalhos
"""
from random import shuffle
primeiro_aluno = input('Digite o primeiro aluno: ')
segundo_aluno = input('Digite o segundo aluno: ')
terceiro_aluno = input('Digite o terceiro aluno: ')
quarto_aluno = input('Digite o quarto aluno: ')
lista = [primeiro_aluno, segundo_aluno, terceiro_aluno, quarto_aluno]
shuffle(lista)
print('A ordem de apresentação será: ')
print(lista)
