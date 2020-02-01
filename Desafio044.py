# elabore um programa que calcule o valor a ser pago por um produto
#, considerando o seu preço normal e condição de pagamento:

# - A vista dinheiro/cheque: 10% de desconto
# - A vista no cartão: 5% de desconto
# - Em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros

val = float(input('Digite o valor do produto: '))

print('-/-'*40)
print('\n[1] - A vista dinheiro ou cheque com 10% desconto')
print('[2] - A vista no cartão de crédito com 5% desconto')
print('[3] - 2x no cartão de crédito sem desconto')
print('[4] - 3x no cartão de crédito com 20% de juros')
print('\n')
print('-/-'*40)
opcao = int(input('\nEscolha a forma de pagamento: '))

if opcao == 1:
    print('\nPagando R${:.2f} a vista o valor será R${:.2f}'.format(val, val - (val*0.1)))
elif opcao == 2:
    print('\nPagando R${:.2f} no cartão e crédito o valor será R${:.2f}'.format(val, val - (val * 0.05)))
elif opcao == 3:
    print('\nPagando R${:.2f} no cartão de crédito o valor da parcela será 2x de R${:.2f}'.format(val, val/2))
elif opcao == 4:
    print('\nPagando R${:.2f} no cartão de crédito com juros de 20% o valor da parcela será 3x de R${:.2f}'.format(val, (val + (val * 0.2))/3))
