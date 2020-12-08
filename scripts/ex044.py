"""Escreva um programa que calcula o calor a ser vapo por um produto, considerando o seu preço normal e condição de pagamento
"""
print('{:=^40}'.format(' CASAS BAHIA '))
valor_produto = float(input('Preço do produto desejado R$ '))
print("""Qual será a forma de pagamento?

\033[1m[1]\033[1m à vista, dinheiro ou cheque
\033[1m[2]\033[1m à vista, no cartão
\033[1m[3]\033[1m até 2x, no cartão
\033[1m[4]\033[1m 3x ou mais, no cartão 
""")
opcao = int(input('Digite a opção desejada: '))
if opcao == 1:
    #desconto concedido para pagamento à vista no dinheiro ou cheque é de 10%
    desconto_dinheiro = valor_produto * 0.10
    desconto_produto_dinheiro = valor_produto - desconto_dinheiro
    print('O valor do produto é de R$ {:.2f}. Com o desconto de R$ {:.2f}. O total a pagar é R$ {:.2f}.'.format(valor_produto, desconto_dinheiro, desconto_produto_dinheiro))
elif opcao == 2:
    #desconto concedido para pagamento à vista no cartão é de 5%
    desconto_cartao = valor_produto * 0.05
    desconto_produto_cartao = valor_produto - desconto_cartao
    print('O valor do produto é de R$ {:.2f}. Com o desconto de {:.2f}. O total a pagar é de R$ {:.2f}.'.format(valor_produto, desconto_cartao, desconto_produto_cartao))
elif opcao == 3:
    #não haverá desconto
    print('O total a pagar é de R$ {:.2f}.'.format(valor_produto))
elif opcao == 4:
    #será acrescido 20 %
    juros = 20
    juros_produto = valor_produto * 1.20
    print('O valor do produto é de R$ {:.2f}. Com o juros de {} %. O total a pagar é de R$ {:.2f}.'.format(valor_produto, juros, juros_produto))
    parcelas_pagamento = float(input('Digite em quantas parcelas deseja pagar: '))
    valor_parcelas = juros_produto / parcelas_pagamento
    print('O valor de cada parcela é de R$ {:.2f}.'.format(valor_parcelas))
else:
    print('Opção \033[1;31mINVÁLIDA\033[m')



