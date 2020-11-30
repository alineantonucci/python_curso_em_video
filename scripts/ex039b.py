"""Fazer um program que ao inserir os dados, ele informe quanto tempo falata para o alistamento
"""
#Esclher a opção do de sexo do usuário
print("""Informe seu sexo abaixo:
[1] Feminino
[2] Masculino""")
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('Você \033[1;31m Não \033[m precisa se alistar')
else:
    print('Ok!')
#Importar o ano atual
from datetime import date
data_atual = date.today().year
data_nasc = int(input('Digite seu ano de nascimento: '))
idade_alistamento = data_atual - data_nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(data_nasc, idade_alistamento, data_atual))
if idade_alistamento == 18:
    print('VocÊ tem que se alistar IMEDIATAMENTE.')
elif idade_alistamento <18:
    saldo_idade = 18 - idade_alistamento
    print('Ainda faltam {} anos para o alistamento.'.format(saldo_idade))
    ano = data_atual + saldo_idade
    print('Seu alistamento será em {}.'.format(ano))
else:
    saldo_idade = idade_alistamento - 18
    print('VocÊ já deveria ter se alistado há {} anos.'.format(saldo_idade))
    ano = data_atual - saldo_idade
    print('Seu alistamento foi em {}.'.format(ano))
