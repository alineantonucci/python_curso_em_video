"""Programa que lê a velocidade de um carro. Se ele ultrapasar 80Km/h,
mostre uma mensagem dizendo que ele foi multado. A multa vai custar
R$7,00 por cada Km acima do limite"""

condutor = float(input('Qual a sua velocidade? '))
if condutor <= 80:
    print('Tenha um bom dia! Dirija com cuidado!')
else:
    condutor_multado = (condutor - 80) * 7.00 #calcular o valor da multa
    print('Você foi MULTADO em R$ {:.2f} reais'.format(condutor_multado))
print('---Fim---')
