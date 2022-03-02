'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai
se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''

import datetime
nascimento = int(input('Qual seu ano de nascimento?'))

# pegando a data atual (de hoje)
data_atual = datetime.date.today()

# pegando o ano atual
ano = int(data_atual.strftime('%Y'))

idade = ano - nascimento
# quantos anos falta ou ja passou
passou = idade - 18

# ano que seria o alistamento
falta = ano - passou

if idade == 18:
    print('Quem nasceu no ano de {} tem {} anos'.format(nascimento, idade))
    print('Você deve fazer o alistamento militar \033[1;31mIMEDIATAMENTE\033[m')
elif idade > 18:
    print('Quem nasceu no ano de {} tem {} anos'.format(nascimento, idade))
    print('Você ja deveria ter feito o alistamento militar a {} anos, que seria no ano de {}'.format(passou, falta))
else:
    print('Você tem {} anos e vai ter que fazer o alistamento militar em {} anos,'.format(idade, passou), end=' ')
    print('que será no ano de {}'.format(falta))
