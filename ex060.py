'''Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:

5! = 5 x 4 x 3 x 2 x 1 = 120'''

n = int(input('Digite um numero para calcular seu fatorial: '))
c = n
f = 1
print('Calculando o Fatorial de {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end=' ')
    print('x 'if c > 1 else '=', end='')
    f = f * c
    c = c - 1
print(' {}'.format(f))

# eu não soube fazer
