# Escreva um programa que leia dois numeros inteiros e compare-os,
# mostrando na tela uma mensagem:

# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais

a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))

if a > b:
    print('O primeiro valor {} é maior'.format(a))
elif a < b:
    print('O segundo valor {} é maior'.format(b))
elif a == b:
    print('Não existe o maior, os dois valores são iguais')