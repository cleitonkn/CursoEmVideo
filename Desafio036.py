# Escreva um programa para aprovar o emprestimo bancario
# para a compra de uma casa. O programa vai pergujntar o valor da casa,
# o salario do comprador e em quantos anos ele vai pagar.

# Calcule o valor da prestação mensal, sabendo que ela não pode exceder
# 30% do salario ou então o emprestimo será negado.

print("-*-"*20)
print('Bem Vindo ao Minha Casa Minha Vida')
print("-*-"*20)

casa = float(input('Qual o valor da casa que deseja financiar? '))
sal = float(input('Qual o seu salário bruto? '))
anos = int(input('Em quantos anos pretende pagar o financiamento? '))

parc = casa/(anos*12)
lim = (sal*0.3)

if parc <= lim:
    print('\nO seu financiamento foi aprovado, o valor da parcela é de R${:.2f}'.format(parc))
else:
    print('\nNós sentimos muito, mas o seu financiamento não pode ser concedido')
print('Obrigado por escolher a Caixa!')