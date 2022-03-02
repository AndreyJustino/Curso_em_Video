# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

frase = str(input('Digite uma frase: ')).strip().upper()  # APOS A SOPA

# juntando uma frase
lista = frase.split()  # separo a frase em uma lista
junto = ''.join(lista)  # coloco todas as palavras da lista junta (coladas)

inverso = junto[::-1]  # jeito mais facil de inverte uma frase

# fazendo ela ser lida de trás para frente
#na parte do "len(junto) - 1" é da onde ele vai começa a mostra as letras

'''inverso = ''
for letra in range(len(junto) - 1, -1, -1):  # aonde começa, onde termina e se pula pra frente ou para trás
    inverso = inverso + junto[letra]'''

# se vai ou não se palindroma
if inverso == junto:
    print('Essa frase é \033[1;92mPALÍNDROMA\033[m')
else:
    print('Essa frase \033[1;91mNÃO\033[m é PALÍNDROMA')
