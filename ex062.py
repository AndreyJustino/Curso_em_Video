'''Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerrará quando ele disser que quer mostrar 0 termos'''

print('\033[1;93mInicialmente resolvendo os 10 primeiros termo de uma PA\033[m')

primeiro = int(input('Qual o primeiro termo da PA? '))
razao = int(input('Qual a razão? '))
termo = primeiro
conta = 1
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while conta <= total:
        print('{} -> '.format(termo), end='')
        termo = termo + razao
        conta = conta + 1
    print('\033[1;31mSTOP\033[m')
    mais = int(input('Quantos termos a mais você quer mostra? (Para acabar de vez, basta digitar 0 )'))

print('\033[1;94m-=-\033[m' * 20)
print('\033[1;31mFim do programa...\033[m')


'''mais_termos = ''

while mais_termos != 0:
    mais_termos = int(input('\nQuer continuar? Se sim, até qual termo? (Para acabar basta digita 0 ) '))
    while conta <= mais_termos:
        print('{} -> '.format(termo), end='')
        termo = termo + razao
        conta = conta + 1
        if mais_termos == 0:
            print('\033[1;91mOk, paramos aqui.\033[m')
print('\033[1;31mOk, paramos aqui.')'''
