'''Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher
qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.'''

print('\033[1;36m-=-\033[m' * 20)
n1 = int(input('Digite um número inteiro:'))
print('Escolha qual será a base de conversão: ')
print('\033[1;92mBinário\033[m [ 1 ]')
print('\033[1;92mOctal\033[m [ 2 ]')
print('\033[1;92mHexadecimal\033[m [ 3 ]')
print('\033[1;31mFechar o programa\033[m [ 4 ]')
opcao = int(input('Qual a sua escolha?: '))
print('\033[1;36m-=-\033[m' * 20)
if opcao == 4:
    print('\033[1;31mPrograma fechado...\033[m')
elif opcao == 1:
    print('Na forma binária fica da seguinte maneira:', bin(n1)[2:])
elif opcao == 2:
    print('Na forma octal fica da seguinte maneira:', oct(n1)[2:])
elif opcao == 3:
    print('Na forma hexadecimal fica da seguinte maneira:', hex(n1)[2:])
else:
    print('\033[1;31mVocê digitou algum outro número que não estava entre as opções...\033[1;31m')
