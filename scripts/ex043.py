"""Desenvolva um programa que leia o peso e a altura, calcule o IMC e mostre ao usuário
"""
#Entrada de dados do usuário
altura = float(input('Qual é a sua altura? (m) '))
peso = float(input('Qual é o seu peso? (Kg) '))
#Cácuo de IMC - índice de massa corpórea
imc = peso / (altura * altura)
if imc < 18.5:
    print('Seu IMC é {:.2f}. Você está ABAIXO DO PESO ideal'.format(imc))
elif imc <= 25:
    print('Seu IMC é {:.2f}. Você está COM O PESO IDEAL'.format(imc))
elif imc <= 30:
    print('Seu IMC é {:.2f}. Você está com OBESIDADE, cuidado'.format(imc))
else:
    print('Seu IMC é {:.2f}. Você está com OBESIDADE MÓRBIDA, procure um médico'.format(imc))
