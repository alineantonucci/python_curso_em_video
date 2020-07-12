# Criar um algorítimo que leia um número e mostre seu dorbro, seu triplo e sua raíz quadrada

n1 = float(input('Digite um número: '))
raiz = n1 ** (1/2)
dobro = n1 * 2
triplo = n1 * 3
print('A raíz quadrada de {}, é {:.2f}.\nO dobro de {}, é {}.\nO triplo de {}, é {}.'.format(n1,raiz,n1,dobro,n1,triplo))
