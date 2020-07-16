""" Ler os nomes dos alunos, sortear um aluno e escrever o nome do aluno na tela
"""

import random
primeiro_aluno = input('Primeiro aluno: ')
segundo_aluno = input('Segundo aluno: ')
terceiro_aluno = input('Terceiro aluno: ')
quarto_aluno = input('Quarto aluno: ')
lista = [primeiro_aluno, segundo_aluno, terceiro_aluno, quarto_aluno]
print('O aluno escolhido foi: {}'.format(random.choice(lista)))
