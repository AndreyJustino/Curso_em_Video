# leia o nome de alguem e diga se ela tem 'silva' entre o nome
nome = str(input('Qual seu nome completo?')).strip().lower().split()
print('Vamos ver se entre o seu nome tem "Silva": {}'.format('silva' in nome))
