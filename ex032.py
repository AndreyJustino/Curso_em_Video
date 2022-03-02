'''Faça um programa que leia um ano qualquer e mostre se ele é bissexto.'''

from datetime import date
ano = int(input('Digite um ano para saber se é bissexto (Digite 0 para analizar o ano atual):'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0: #CONDIÇÃO PARA SABE SE É BISSEXTO
    print('O ano de {} é bissexto'.format(ano))
else:
    print('O ano de {} NÃO é bissexto'.format(ano))
