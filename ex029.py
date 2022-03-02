'''Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.'''

from time import sleep
velocidade = float(input('Qual a velocidade do carro em Km?:'))
multa = (velocidade - 80) * 7.00 #calculo da multa se passa de 80 km
print('Se passar de 80 Km/h você será multado.')
print('PROCESSANDO...')
sleep(4)
if velocidade <= 80:
    print('Você não será multado. Continue assim!')
else:
    print('Você passou de 80 km/h. Sua multa é de R${:.2f}'.format(multa))
