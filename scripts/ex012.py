# Criar um programa que calcula o desconto

produto = float(input('Qual é o preço do produto? R$ '))
print('O produto que custava R$ {}, na prommoção com desconto de 5% vai custar R$ {:.2f}'
      .format(produto, produto*0.95))
