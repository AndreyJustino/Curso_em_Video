#cria um programa que leia um numero real (com virgula) e que mostre sua parte inteira sem a virgula
from math import trunc
n1 = float(input('Digite uma número com virgula(ponto):'))
print('O numero digitado foi {} e sua parte inteira é {}'.format(n1, trunc(n1)))
