print('Em uma liquidação todos os produtos estão com 5% de desconto')
preco = float(input('Digite o preço de um produto: R$'))
descon = preco - (preco * 5 / 100)
print('Com o desconto de 5% o produto sai por {:.2f}'.format(descon))
