'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.'''

print('\033[1;33m-=-\033[m' * 20)
valor = float(input('Qual o valor do empréstimo que você deseja? R$'))
salario = float(input('Qual o valor do seu sálario? R$'))
anos = int(input('Em quantos \033[1;31mANOS\033[m você pretende pagar?'))
print('\033[1;33m-=-\033[m' * 20)
prestacao = valor / (anos * 12)
exceder = salario * 30/100
if prestacao >= exceder:
    print('\033[1;31mNão\033[m poderá ser feito o empréstimo ')
    print('O valor da prestação seria R${:.2f} '.format(prestacao))
else:
    print('\033[1;32mPoderá\033[m ser feito o empréstimo')
    print('O valor das prestações são R${:.2f}'.format(prestacao))
