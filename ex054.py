# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda
# não atingiram a maioridade e quantas já são maiores.

from datetime import date
conta = 0
conta2 = 0
atual = date.today().year

# coletando dados e separando eles em maior e menor idade
for c in range(1, 7 + 1 ):
    ano = int(input('Qual ano de nascimento da {}º pessoa? '.format(c)))
    idade = atual - ano
    if idade >= 18:
        conta = conta + 1  # quantas atingiram a maior idade
    elif idade <= 17:
        conta2 = conta2 + 1  # quantas não atingiram a maior idade

# mensagem mostrando os dados
print('\033[1;93m-=-\033[m' * 20)
print('''Apenas {} pessoas atingiram a maior idade. '''
'''\nAinda faltam {} pessoas para atingir a maior idade.'''.format(conta, conta2))
print('\033[1;93m-=-\033[m' * 20)
