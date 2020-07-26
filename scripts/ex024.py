"""Crie um programa que leia o nome de uma cidade e dig se ela começa ou não
com o nome 'SANTO'
"""
cidade = str(input('Em qua cidade você nasceu? ')).strip()
print(cidade[:5].upper() == 'SANTO')