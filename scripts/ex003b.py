#Programa que lê números e faz a soma a média entre eles com cores no terminal

valor1 = float(input('\033[1;31m Digite um valor: \033[m'))
valor2 = float(input('\033[1;31m Digite outro valor: \033[m'))
soma = valor1 + valor2
media = soma / 2
print('\033[1;30;41m A média entre {} e {} é igual a:  {}\033[m'.format(valor1,valor2,media))


