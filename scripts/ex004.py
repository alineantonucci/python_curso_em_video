# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo rpomitivo e todas as informações possíveis

a = input('Digite algo: ')
print('Isso é um número? ', a.isnumeric())
print('Isso é um título? ', a.istitle())
print('Está em letras maiúsculas? ', a.isupper())
print('Está em decimal? ', a.isdecimal())
print('É alfa numérico? ', a.isalnum())