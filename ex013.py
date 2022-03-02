print('Você ganhou um aumento no salario de 15%!')
salari = float(input('Quando era o seu antigo salario?:R$'))
aumento = salari + (salari * 15 / 100)
print('Seu salario atual é R${:.2f}'.format(aumento))
