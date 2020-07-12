""" Escreva um programa que pergunte a qunatidade de Km percorridos por um carro
alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a
pagar, sabendo que o carro custa R$60/dia e R$0,15/km rodado
"""

dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
preçodia = (dias * 60)
preçokm = (km * 0.15)
print('O total a pagar é de R$ {:.2f}.'
      .format(preçodia+preçokm))
