'''Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
de acordo com a média atingida:

– Média abaixo de 5.0: REPROVADO

– Média entre 5.0 e 6.9: RECUPERAÇÃO

– Média 7.0 ou superior: APROVADO'''

nota1 = float(input('Qual a primeira nota: '))
nota2 = float(input('Qual a segunda nota?: '))
media = (nota1 + nota2) / 2
if media < 5.0:
    print('A média do aluno foi {:.1f}, portanto ele foi \033[1;31mREPROVADO\033[m'.format(media))
elif media == 5.0 or media <= 6.9:
    print('A média do aluno foi {:.1f}, portando ele esta de \033[1;33mRECUPERAÇÃO\033[m' .format(media))
elif media >= 7.0:
    print('A média do aluno foi {:.1f}, portando ele foi \033[1;32mAPROVADO\033[m'.format(media))
