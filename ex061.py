'''Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da
progressão usando a estrutura while.'''

primeiro = int(input('Qual o primeiro termo da PA? '))
razao = int(input('Qual a razão? '))
termo = primeiro
conta = 1
while conta <= 10:
    print('{} -> '.format(termo), end='')
    termo = termo + razao
    conta = conta + 1
print('Concluído')
