# Escreva um programa que pergunte o
# salário de um funcionário e calcule
# o valor do seu aumento.
# Para salários superiores a R$1250,00,
# calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento
# é de 15%

salario = float(input('Digite o seu salário atual: '))
if salario >= 1250:
    print('Seu novo salário com acrescimo de 10% será de R${:.2f}'.format(salario+(salario*0.1)))
else:
    print('Seu novo salário com acrescimo de 15% será de R${:.2f}'.format(salario+(salario*0.15)))
