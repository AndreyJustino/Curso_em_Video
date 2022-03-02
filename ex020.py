#leia 4 nomes e sorteie uma ordem aleatoria desses nomes (esse nomes são de alunos)

from random import shuffle

a1 = input('Nome do primeiro aluno:')
a2 = input('Nome do segundo aluno:')
a3 = input('Nome do terceiro aluno:')
a4 = input('Nome do quarto aluno')
lista = [a1, a2, a3, a4]
shuffle(lista)
print('A ordem é a seguinte:', lista)

#esse codigo acima cria uma lista com os 4 nomes em uma ordem aleatoria
