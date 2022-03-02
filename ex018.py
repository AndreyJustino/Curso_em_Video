#leia um angulo e calcule o seno, cosseno e a tangente

from math import sin, cos, tan, radians
ang = float(input('Digite o valor do angulo:'))
seno = sin(radians(ang))
cosseno = cos(radians(ang))
tangente = tan(radians(ang))
print('O angulo é {} e o seu SENO  é {:.2f}'.format(ang, seno))
print('O angulo é {} e o seu COSSENO  é {:.2f}'.format(ang, cosseno))
print('O angulo é {} e a sua TANGENTE  é {:.2f}'.format(ang, tangente))
