'''Escreva um programa que pergunte o salário de um funcionário
e calcule o valor do seu aumento. Para salários superiores a R$1250,00,
calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.'''

salario = float(input('Qual é o valor de seu sálario? R$'))
if salario > 1250.00:
    aumento = salario * 10 / 100
    print('Você sofreu um aumento de 10%, seu salário atual é {:.2f}'.format(salario + aumento))
else:
    aumento = salario * 15 / 100
    print('Você sofreu um aumento de 15%, seu salário atual é {:.2f}'.format(salario + aumento))
