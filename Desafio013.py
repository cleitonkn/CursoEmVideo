sal = float(input('\nDigite o salário do funcionário: '))
aum = 15
conv = aum/100
valor = sal + (sal*conv)

print('\nO novo salário do funcionario com aumento de {}% é igual a {:.2f}'.format(aum, valor))