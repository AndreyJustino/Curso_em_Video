'''Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.'''

from random import randint

sorteado = randint(0, 10)
conta = 1
continuar = ''.strip().upper()

print('\033[1;93m-=-\033[m' * 20)

print('Adivinhe o número que estou pensando entre 0 e 10.')

print('\033[1;93m-=-\033[m' * 20)

tentativa = int(input('Digite o número que você acredita ser:'))

if tentativa != sorteado:
    continuar = str(input('Você errou! Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'S':
        while tentativa != sorteado and continuar == 'S':
            tentativa = int(input('Ok. Tente mais uma vez: '))
            conta = conta + 1
            if tentativa != sorteado and sorteado < tentativa:
                print('Você errou! O número é menor que esse...')
                continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
                if continuar in 'Nn':
                    print('Você perdeu por \033[1;31mDESISTENCIA!\033[m')
            elif tentativa != sorteado and sorteado > tentativa:
                print('Você errou! O número é maior que esse...')
                continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
                if continuar in 'Nn':
                    print('Você perdeu por \033[1;31mDESISTENCIA!\033[m')
            else:
                print('Você acertou! \033[1;92mParabéns!\033[m Preciso de apenas {} tentativa'.format(conta))
    else:
        print('Você perdeu por \033[1;31mDESISTENCIA!\033[m')
else:
    print('Você acertou! \033[1;92mParabéns!\033[m Preciso de apenas {} tentativa'.format(conta))
print('\033[1;93m-=-\033[m' * 20)
