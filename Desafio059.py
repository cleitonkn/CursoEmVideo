'''Crie um programa que leia dois valores e mostre um menu na tela:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.
'''
import math
num1 = float(input('Digite o primeiro valor: '))
num2 = float(input('Digite o segundo valor: '))
opcao = 0
while opcao != 5:
    print('//////////////////MENU//////////////////////////')
    print('\nSelecione uma das opções:\n')
    print('[1] somar')
    print('[2] mutiplicar')
    print('[3] maior')
    print('[4] novos números')
    print('[5] sair do programa')
    opcao = int(input())
    if opcao == 1:
        print('a soma entre os números {} e {} é igual a {}\n'.format(num1, num2, num1+num2))
        print('Digite qualquer numero ou letra para retornar ao menu inicial')
        input()
    if opcao == 2:
        print('a multiplicação entre os números {} e {} é igual a {}\n'.format(num1, num2, num1*num2))
        print('Digite qualquer numero ou letra para retornar ao menu inicial')
        input()
    if opcao == 3:
        if num1 > num2:
            print('O maior número entre o primeiro valor {} e o segundo valor {} é {}\n'.format(num1, num2, num1))
        elif num1 == num2:
            print('o primeiro valor {} e o segundo valor {} são iguais\n'.format(num1, num2))
        else:
            print('O maior número entre o primeiro valor {} e o segundo valor {} é {}\n'.format(num1, num2, num2))
        print('Digite qualquer numero ou letra para retornar ao menu inicial')
        input()
    if opcao == 4:
        num1 = float(input('Digite o primeiro valor: '))
        num2 = float(input('Digite o segundo valor: '))
