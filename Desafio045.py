# crie um programa que faça o computador jogar Jokenpô com você.

import random

print('*'*40)
print('Ecolha um das opções: ')
print('*'*40)
print('Pedra')
print('Papel')
print('Tesoura')

print('*'*40)
eu = str(input('Digite uma das opção: '))
lista = ['Pedra', 'Papel', 'Tesoura']
maq = random.choice(lista)
print('*'*40)

if eu == maq:
   print('Você: {}, Máquina: {}. Empate! Na próxima você ganha.'.format(eu,maq))
if eu == 'Papel' and maq == 'Pedra':
    print('Você: {}, Máquina: {}. Você ganhou!'.format(eu, maq))
if eu == 'Pedra' and maq == 'Tesoura':
    print('Você: {}, Máquina: {}. Você ganhou!'.format(eu, maq))
if eu == 'Tesoura' and maq == 'Papel':
    print('Você: {}, Máquina: {}. Você ganhou!'.format(eu, maq))
if eu == 'Papel' and maq == 'Tesoura':
    print('Você: {}, Máquina: {}. Você Perdeu! Na próxima você ganha.'.format(eu, maq))
if eu == 'Pedra' and maq == 'Papel':
    print('Você: {}, Máquina: {}. Você Perdeu! Na próxima você ganha.'.format(eu, maq))
if eu == 'Tesoura' and maq == 'Pedra':
    print('Você: {}, Máquina: {}. Você Perdeu! Na próxima você ganha.'.format(eu, maq))