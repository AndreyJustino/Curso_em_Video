# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”
nome = input('Qual o nome da sua cidade?').strip().capitalize()
print('Vamos ver se o nome da sua cidade começa com "SANTO"')
primeiro = nome.split()
print('Santo' in primeiro[0])

