#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 0
for c in range(1, 5 + 1):
    peso = float(input('Qual o peso da {}º pessoa? '.format(c)))
    if peso == 1:
        maior = peso
        menor = peso
    else:
        if peso >= maior:
            maior = peso
        if peso <= menor:
            menor = peso
print('''O maior peso é {}. 
Já o menor é {}'''.format(maior, menor))

