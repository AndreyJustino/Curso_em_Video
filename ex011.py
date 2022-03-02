altu = float(input('Quantos metro de altura tem sua parede?:'))
largu = float(input('E quantos metros de largura tem sua parede?:'))
area = altu * largu
print('Sua parede tem {}x{}, portanto sua área é {}m².'.format(largu, altu, area), end='')
print('E como a cada 2m² é um litro de tinta, você vai precisar de {}'.format(area / 2))
