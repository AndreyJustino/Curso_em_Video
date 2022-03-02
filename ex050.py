'''Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
Se o valor digitado for ímpar, desconsidere-o'''

acumu = 0
conta = 0
for c in range(1, 7):
    n1 = int(input('Digite o {}º número: '.format(c)))
    par = n1 % 2
    if par == 0:
        acumu = acumu + n1
        conta = conta + 1
print('Você digitou {} número PAR/PARES e a soma de todos os números PARES digitados é {}.'.format(conta, acumu))
