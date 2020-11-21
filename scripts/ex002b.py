# Criar um programa de boas vindas ao usuário, como cores no terminal

print('\033[1;30;46m  *  \033[m'*20)
nomeusuario = input('\033[1;36m Digite seu nome: \033[m')
print('\033[1;46m É um prazer te conhecer {}! \033[m'.format(nomeusuario))
