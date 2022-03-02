# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

num = int(input('Informe uma numeração:'))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Observando o numero {}'.format(num))
print('A unidade desse numero é {}'.format(u))
print('A dezena desse numero é {}'.format(d))
print('A centena desse numero é {}'.format(c))
print('A milhar desse numero é {}'.format(m))
