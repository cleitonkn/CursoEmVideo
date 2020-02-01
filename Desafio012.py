preco = float(input('Digite o preço do produto: '))
desc = int(input('Digite o valor do desconto: '))
conv = desc/100
valor = preco - (preco*conv)

print('O valor do produto com desconto de {}% é igual a {:.2f}'.format(desc, valor))
