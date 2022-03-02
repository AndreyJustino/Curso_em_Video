'''Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
Caso esteja errado, peça a digitação novamente até ter um valor correto.'''

# minha maneira, que tambem esta correta
'''sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Qual seu sexo? [M/F] ')).upper().strip()[0]
    if sexo != 'M' and sexo != 'F':
        print('Responda conforme as opções dadas! \033[1;31m[M/F]\033[m')
    else:
        print('Obrigado por responder corretamente!')
print('Sexo {} registrado com \033[1;92msucesso!\033[m'.format(sexo))'''

# maneira do professor que tambem esta correta
sexo = str(input('Qual seu sexo? [M/F] ')).upper().strip()[0]
while sexo not in 'MF':
    sexo = str(input('\033[1;31mResposta inválida!\033[m Por favor, tente novamente [M/F]: ')).upper().strip()[0]
print('Sexo {} registrado com \033[1;92msucesso\033[m'.format(sexo))
