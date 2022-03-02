# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

n = int(input("Verificar se é um numero primo: "))
conta = 0

for c in range (1, n +1):  # conta do 1 até o número escolhido
    if n % c == 0:  # se N for dividido por C e for igual a 0
        print('\033[1;31m', end='')  # pinta de vermelho
        conta = conta + 1  # e soma mais um no contador
    else:
        print('\033[1;36m', end='')  # se não pinta de azul
    print('{} '.format(c), end='')  # aqui ele vai mostra quais estão azul e quais estão vermelho

print('\n\033[;1mO número {} foi dividido {} vezes.\033[m'.format(n, conta))  # quantidade de vezes que N foi dividido

if conta == 2:  # se o número for dividido somente duas vezes e o contador tiver marcado 2 ele é primo
    print('Esse é um número \033[1;92mprimo\033[m.')
else:
    print('Esse \033[1;31mnão\033[m é um número primo') # se for mais de 2 ou menos de dois não é primo
