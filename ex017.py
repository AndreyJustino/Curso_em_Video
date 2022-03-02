#cria uma programa que leia o cateto adjacente e oposto e calucule o valor da hipotenusa
#o comando pow é significa a mesma coisa que a potencia

'''from math import pow, sqrt
cateAdja = float(input('Digite o valor do cateto adjacente:'))
cateOpos = float(input('Digite o valor do cateto oposto:'))
hipo = sqrt(pow(cateAdja, 2) + pow(cateOpos, 2))
print('O valor da hipotenusa é {:.2f}'.format(hipo))'''

from math import hypot
cateAdja = float(input('Digite o valor do cateto adjacente:'))
cateOpos = float(input('Digite o valor do cateto oposto:'))
hi = hypot(cateOpos, cateAdja)
print('O valor da hipotenusa é {:.2f}'.format(hi))
