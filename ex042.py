'''Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

– EQUILÁTERO: todos os lados iguais

– ISÓSCELES: dois lados iguais, um diferente

– ESCALENO: todos os lados diferentes'''

print('\033[1;36m-=-\033[m' * 20)
reta1 = float(input('Qual o comprimento da primeira reta?'))
reta2 = float(input('Qual o comprimento da segunda reta?'))
reta3 = float(input('Qual o comprimento da terceira reta?'))
print('\033[1;36m-=-\033[m' * 20)

# verificando se é possivel forma um triangulo
if reta1 <= reta2 + reta3 and reta2 <= reta1 + reta3 and reta3 <= reta1 + reta2:
    print('É POSSIVEL forma um TRIÂNGULO')
# se for possivel, vai verificar o tipo de triangulo
    if reta1 == reta2 == reta3:
        print('Esse é um triângulo EQUILATERO')
    elif reta1 != reta2 and reta2 != reta3 and reta3 != reta1:
        print('Esse é um triângulo ESCALENO')
    else:
        print('Esse é um triângulo ISÓCELES')
else:
    print('NÃO é possivel forma um triângulo')
print('\033[1;36m-=-\033[m' * 20)
