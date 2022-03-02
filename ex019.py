#cria um programa que sorteie um nome entre os de 4 alunos para apagar o quadro

from random import choice
a1 = input('Nome do primeiro aluno:')
a2 = input('Nome do segundo aluno:')
a3 = input('Nome do terceiro aluno:')
a4 = input('Nome do quarto aluno:')
print('O sorteado foi {}'.format(choice([a1, a2, a3, a4])))
