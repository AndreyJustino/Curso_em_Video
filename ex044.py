'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e
condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço formal

– 3x ou mais no cartão: 20% de juros'''

print('\033[1;33m-=-\033[m' * 20)
preço = float(input('Qual o preço do produto? R$'))
print('Escolha a forma de pagamento')
print('[ 1 ] Dinheiro ou Cheque')
print('[ 2 ] À vista no cartão')
print('[ 3 ] Em até 2x no cartão')
print('[ 4 ] Em até 3x ou mais no cartão')
print('[ 0 ] Cancelar pagamento')
condição = int(input('Digite a opção escolhida: '))
print('\033[1;33m-=-\033[m' * 20)
if condição == 1:
    calculo = preço - (preço * 10 / 100)
    print('Como será pago em dinheiro, recebera o desconto de 10%. Preço a pagar é R${}'.format(calculo))
elif condição == 2:
    calculo = preço - (preço * 5 / 100)
    print('Como será à vista no cartão, recebera o desconto de 5%. Preço a pagar é R${}'.format(calculo))
elif condição == 3:
    print('Como será em 2x no cartão, segue o preço formal {}. Pagara por 2 meses R${}'.format(preço, preço / 2))
elif condição == 4:
    parcela = int(input('Quer parcela em quantas vezes no cartão? (\033[;1mAO ESCOLHER ESSA OPÇÃO SOMA 20% DE JUROS\033[m)'))
# quanto vão preço total, somando com o juros
    total = preço + (preço * 20 / 100)
# quanto vão pagar por mes
    mes = total / parcela
    print('Sua compra que foi parcelada em {}x de {:.2f} COM JUROS'.format(parcela, mes))
    print('Tem o total a pagar de R${:.2f}'.format(total))
elif condição == 0:
    print('Pagamento \033[1;31mCANCELADO\033[m')
else:
    print('\033[;1mOPÇÃO INVALIDA\033[m')
print('\033[1;33m-=-\033[m' * 20)
