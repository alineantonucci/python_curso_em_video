"""Fazer um progrma que mostre na tela uma contagem regressiva para o estouro de fogos de artifício
"""

#importar biblioteca de tempo
from time import sleep
#entrada dos dados
ano = int(input('Digite o ano para começar a contagem regressiva: '))
for cont in range(10, -1, -1):
    print(cont)
    sleep(1)
print('F')
print('E')
print('L')
print('I')
print('Z')
print('{}'.format(ano))
