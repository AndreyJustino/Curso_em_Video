'''Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km
e R$0,45 parta viagens mais longas.'''

distancia = float(input('Qual é a distancia em Km de sua viagem?'))
padrao = 0.50 * distancia
longa = 0.45 * distancia
if distancia <= 200:
    print('O preço da sua passagem é de R${:.2f}'.format(padrao))
else:
    print('O preço da sua passagem é de R${:.2f}'.format(longa))
