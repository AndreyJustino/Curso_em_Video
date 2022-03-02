print('Vou calcular o aluguel do seu carro, mas antes responda:')
dia = int(input('Quantos dias você uso o carro?'))
km = float(input('Quantos Km você rodo?'))
print('Você vai pagar R${:.2f}'.format((dia * 60) + (0.15 * km)))
