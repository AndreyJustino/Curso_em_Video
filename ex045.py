# Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
print('====== Vamos jogar \033[1;36mJOKENPÔ\033[m ======')
print('''Escolha alguma das opções abaixo:
[ 1 ] Papel
[ 2 ] Tesoura
[ 3 ] Pedra
[ 0 ] \033[1;31mDesistir\033[m''')
jogador = int(input('Qual você escolhe? '))
print('=' * 33)
computador = randint(1, 3)
if jogador == computador:
    print('Houve um \033[1;33mEMPATE\033[m')
elif jogador == 1 and computador == 3:
    print('''PARABÉNS, você \033[1;92mvenceu\033[m! 
Eu joguei PEDRA e você PAPEL''')
elif jogador == 2 and computador == 1:
    print('''PARABÉNS, você \033[1;92mvenceu\033[m! 
Eu joguei PAPEL e você TESOURA''')
elif jogador == 3 and computador == 2:
    print('''PARABÉNS, você \033[1;92mvenceu\033[m! 
Eu joguei TESOURA e você PEDRA''')
elif jogador == 0:
    print('Eu venci, pois você \033[1;31mDESISTIU\033[m')
elif computador == 1 and jogador == 3:
    print('''Você \033[1;31mPERDEU\033[m! 
Eu joguei PAPEL e você PEDRA''')
elif computador == 2 and jogador == 1:
    print('''Você \033[1;31mPERDEU\033[m! 
Eu joguei TESOURA e você PAPEL''')
elif computador == 3 and jogador == 2:
    print('''Você \033[1;31mPERDEU\033[m! 
Eu joguei PEDRA e você TESOURA''')
else:
    print('\033[;1mOPÇÃO INVALIDA\033[m')
print('=' * 33)
