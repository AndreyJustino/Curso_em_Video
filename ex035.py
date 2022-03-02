'''Desenvolva um programa que leia o comprimento de
três retas e diga ao usuário se elas podem ou não  formar um triângulo.'''

print('\033[36m-=-\033[m' * 20)
reta1 = float(input('Qual o comprimento da primeira reta?'))
reta2 = float(input('Qual o comprimento da segunda reta?'))
reta3 = float(input('Qual o comprimento da terceira reta?'))
print('\033[1;31m-=-\033[m' * 20)
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('É POSSIVEL forma um TRIÂNGULO')
else:
    print('NÃO é possivel forma um triângulo')
print('\033[1;36m-=-\033[m' * 20)

if reta1 == reta2 and reta2 == reta3 and reta3 == reta1:
    print('Esse é um triângulo EQUILATERO')
elif reta1 != reta2 and reta2 != reta3 and reta3 != reta1:
    print('Esse é um triângulo ESCALENO')
else:
    print('Esse é um triângulo ISÓCELES')
print('\033[31m-=-\033[m' * 20)