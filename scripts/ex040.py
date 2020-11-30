"""Criar um programa que leia as notas do aluno, calcule a média e mostre mensagem finak, de acorodo com a média
atingida pelo aluno
"""

#Entrada das notas
nota1 = float(input('\033[1;mDigite a primeira nota: \033[m'))
if nota1 < 0.0:
    nota1 = float(input('\033[1;mDigite a primeira nota: \033[m'))
nota2 = float(input('\033[1;mDigite a segunda nota: \033[m'))
if nota2 < 0.0:
    nota2 = float(input('\033[1;mDigite a segunda nota: \033[m'))
#soma e média das notas
soma = nota1 + nota2
mediaaluno = soma / 2
#Condição ara executar o programa
if mediaaluno < 5.0:
    print('Sua média é: {}, você está \033[1;31m Reprovado \033[m'.format(mediaaluno))
elif mediaaluno <= 6.9:
    print('Sua média é: {}, você está em \033[1;33m Recuperação \033[m'.format(mediaaluno))
elif mediaaluno > 10.0:
    print('\033[1;30;41m ERRO \033[m')
else :
    print('Sua média é: {}, você está \033[1;36m Aprovado \033[m'.format(mediaaluno))
