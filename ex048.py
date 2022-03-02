""" Faça um programa que calcule a soma entre todos os números que são múltiplos de três e impares
e que se encontram no intervalo de 1 até 500."""

#print(1 % 2) para saber se é impar ou par

# s = 0
# for c in range(1, 501):
#     if c % 2 == 1 and c % 3 == 0:
#         print(c)
#         s = s + c
# print('A soma entre todos os número que são múltiplos de três e ímpares é {}.'.format(s))

acumulador = 0
contador = 0
for c in range(1, 501, 2):
    if c % 3 == 0: # aperte enter e escrva print(c) para mostra todos os numero
        contador = contador + 1
        acumulador = acumulador + c
print('A soma entre todos os número que são múltiplos de três e ímpares é {}.'.format(acumulador))
print('E o total de números encontrados foi {}.'.format(contador))
