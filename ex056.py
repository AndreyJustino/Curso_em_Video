'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.'''

coleta_media = 0
maior_idade = 0
nome = ''
conta = 0

for c in range(1, 4 + 1):
    print('\033[1;33m-------- {}ºPESSOA --------\033[m'.format(c))
    nome1 = str(input('Qual o nome da pessoa? ')).capitalize().strip()
    sexo1 = str(input('Qual o sexo da pessoa? [M/F] ')).upper().strip()
    idade1 = int(input('Qual a idade da pessoa? '))
    coleta_media = coleta_media + idade1
    if sexo1 == 'M':
        if idade1 == 1:
            maior_idade = idade1
            nome = nome1
        else:
            if idade1 >= maior_idade:
                maior_idade = idade1
                nome = nome1
    if sexo1 == 'F':
        if idade1 <= 20:
            conta = conta + 1

media = coleta_media / 4  # media de idade
print('\033[1;33m-\033[m' * 26)
print('A idade média do grupo é {}'.format(media))
print('O nome do homem mais velho do grupo é {}. Sua idade é {}.'.format(nome, maior_idade))
print('Apenas {} mulher/mulheres tem menos ou 20 anos'.format(conta))
print('\033[1;33m-\033[m' * 26)
