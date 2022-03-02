'''Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros
termos dessa progressão.'''

primeiro = int(input('Qual o primeiro termo da PA? '))
razão = int(input('Qual a razão? '))
termo = primeiro + (10 - 1) * razão # pegando o 10º termo, descobrindo até onde ele vai repetir
for c in range(primeiro, termo + razão, razão):
    print(c, end=' -> ')
print('Concluído')

# achei esse exercicio dificil
