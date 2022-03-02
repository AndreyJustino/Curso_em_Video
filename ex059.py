''' Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso. '''

from time import sleep
escolha = ''

print('\033[1;96m-=-\033[m' * 20)
n1 = int(input('Digite um número: '))
n2 = int(input('Digite mais um número: '))
print('\033[1;96m-=-\033[m' * 20)

while not escolha == 5:
    print('''Escolha uma das opções abaixo:
    [ 1 ] Somar os valores
    [ 2 ] Multiplicar os valores
    [ 3 ] Descobrir qual é o maior valor
    [ 4 ] Adicionar novos números
    [ 5 ] Sair do programa''')
    escolha = int(input('Qual a sua escolha? '))
    soma = n1 + n2
    multi = n1 * n2
    maior = 0
    print('\033[1;96m-=-\033[m' * 20)
    if escolha == 4:
        n1 = int(input('Digite um novo número: '))
        n2 = int(input('Digite mais um novo número: '))
        print('\033[1;96m-=-\033[m' * 20)
    elif escolha == 1:
        print('A soma entre os valores é {}'.format(soma))
        print('\033[1;96m-=-\033[m' * 20)
    elif escolha == 2:
        print('A multiplicação entre os valores é {}'.format(multi))
        print('\033[1;96m-=-\033[m' * 20)
    elif escolha == 3:
        if n1 > n2:
            maior = n1
            print('O maior valor é {}'.format(n1))
        elif n2 > n1:
            maior = n2
            print('O maior valor é {}'.format(n2))
        elif n1 == n2:
            print('Os dois valores são iguais')
        print('\033[1;96m-=-\033[m' * 20)
    elif escolha == 5:
        print('\033[1;91mPrograma fechado.\033[m')
        print('\033[1;96m-=-\033[m' * 20)
    else:
        print('\033[;1mOPÇÃO INVALIDA\033[m')
        print('\033[1;96m-=-\033[m' * 20)
    sleep(2)
