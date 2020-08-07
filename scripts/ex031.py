"""Programa que pergunta a distância de uma viagem em Km.
Calcula o preço da passagem, cobrando R$0,50 por Km para viagens até 200Km e
R$0,45 para viagens mais longas"""

passageiro = float(input('Qual á a distância da sua viagem em quilômetros? '))
if passageiro <= 200:
    preco = passageiro * 0.50
else:
    preco = passageiro * 0.45

print('O preço da sua passagem é de: R$ {:.2f}'.format(preco))
print('Tenha uma boa VIAJEM')
