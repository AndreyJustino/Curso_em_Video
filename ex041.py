'''A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre
sua categoria, de acordo com a idade:

– Até 9 anos: MIRIM

– Até 14 anos: INFANTIL

– Até 19 anos: JÚNIOR

– Até 25 anos: SÊNIOR

– Acima de 25 anos: MASTER'''

from datetime import date
nascimento = int(input('Qual o ano do seu nascimento? '))
ano_atual = date.today().year
idade = ano_atual - nascimento
print('A idade do atleta é {}, portanto'.format(idade), end=' ')
if idade <= 9:
    print('a sua categoria é \033[;1mMIRIM\033[m')
elif idade <= 14:
    print('a sua categoria é \033[;1mINFANTIL\033[m')
elif idade <= 19:
    print('a sua categoria é \033[;1mJÚNIOR\033[m')
elif idade <= 25:
    print('a sua categoria é \033[;1mSÊNIOR\033[m')
else:
    print('a sua categoria é \033[;1mMASTER\033[m')
