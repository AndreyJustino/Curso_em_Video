# Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Qual seu nome completo?')).strip()
primeiro = nome.split()
print('Seu primeiro nome é {} e o seu ultimo é {}'.format(primeiro[0], primeiro[len(primeiro)-1]))
