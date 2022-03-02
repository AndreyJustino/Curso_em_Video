"""crie um programa que leia o nome de uma pessoa e mostre :
seu nome todo em maiusculo, minusculo, quantas letras tem ao todo (sem contar os espaço) e quantas letras
tem o primeiro nome"""

nome = str(input('Qual seu nome completo?')).strip()
print('Seu nome em maiusculo é {}'.format(nome.upper()))
print('Seu nome em minusculo é {}'.format(nome.lower()))
print('Seu nome completo tem {} letras'.format(len(nome) - nome.count(' ')))
lista = nome.split()
print('Seu primeiro nome é {} e tem {} letras'.format(lista[0], len(lista[0])))
