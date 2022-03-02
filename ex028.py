'''Escreva um programa que faça o computador “pensar” em um número inteiro
entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido
pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.'''

from random import randint
from playsound import playsound
sorteado = randint(0, 5)
print('\033[33m-=-\033[m' * 20)
print('Adivinhe o número que estou pensando entre 0 e 5.')
print('\033[33m-=-\033[m' * 20)
tentativa = int(input('Digite o número que você acredita ser:'))
if tentativa == sorteado:
    print('Você acertou! \033[1;92mParabéns!\033[m')
else:
    print('\033[1;31mErrou!\033[m O número era {}'.format(sorteado), playsound('y2meta.com - Errou!!! (128 kbps).mp3'))
