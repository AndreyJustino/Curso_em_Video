'''Faça um programa que leia três números e mostre qual é o maior e qual é o menor.'''

n1 = int(input('Digite o primeiro número:'))
n2 = int(input('Digite o segundo número:'))
n3 = int(input('Digite o terceiro número:'))
# descobrindo o maior
if n1 > n2 and n1 > n3:
    maior = n1
if n2 > n3 and n2 > n1:
    maior = n2
if n3 > n2 and n3 > n1 :
    maior = n3
print('O maior número é {}'.format(maior))
# descobrindo o menor
if n1 < n2 and n1 < n3:
    menor = n1
if n2 < n1 and n2 < n2:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print('O menor número é {}'.format(menor))
