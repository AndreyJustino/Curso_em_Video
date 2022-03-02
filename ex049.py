'''Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher,
só que agora utilizando um laço for'''

'''contador = 0
n1 = int(input('Digite um número, que irei fazer a tabuada dele:'))
print('\033[1;96m=\033[m' * 11)
for c in range(1, 11):
    contador = contador + 1
    print('{} x {:2} = {}'.format(n1, contador, n1 * contador))
print('\033[1;96m=\033[m' * 11)'''

n1 = int(input('Digite um número, que irei fazer a tabuada dele:'))
print('\033[1;96m=\033[m' * 11)
for c in range(1, 11):
    print('{} x {:2} = {}'.format(n1, c, n1 * c))
print('\033[1;96m=\033[m' * 11)
