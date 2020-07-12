# Faça um progrma que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor

numero1 = int(input('Digite um número: '))
sucessor = numero1 + 1
antecessor = numero1 - 1
print('O sucessor do número {}, é: {}. \nO antecessor do número {}, é: {}.'.format(numero1,sucessor,numero1,antecessor))