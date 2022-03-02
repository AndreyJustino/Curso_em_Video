'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e
mostre seu status, de acordo com a tabela abaixo:

– IMC abaixo de 18,5: Abaixo do Peso

– Entre 18,5 e 25: Peso Ideal

– 25 até 30: Sobrepeso

– 30 até 40: Obesidade

– Acima de 40: Obesidade Mórbida'''

peso = float(input('Qual o seu peso(Kg)? '))
altura = float(input('E qual é a sua altura(M)? '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('Você esta \033[;1mABAIXO DO PESO\033[m')
elif imc >= 18.5 and imc < 25:
    print('Você esta com o \033[;1mPESO NORMAL\033[m')
elif imc >= 25 and imc < 30:
    print('Você esta em \033[;1mSOBREPESO\033[m')
elif imc >= 30 and imc <= 40:
    print('Você esta em \033[;1mOBESIDADE\033[m  ')
elif imc > 40:
    print('Você esta em \033[;1mOBESIDADE MÓRBIDA\033[m, \033[1;31mcuidado!\033[m')
print('Seu IMC é {:.1f}'.format(imc))
