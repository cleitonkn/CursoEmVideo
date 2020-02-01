''' Melhore o jogo do DESAFIO 028 onde o computador vai pensar em um número
entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando
no final quantos palpites foram necessários para vencer '''

import random
jogador = 11
maquina = 12
while jogador != maquina:
    maquina = random.randrange(0, 11)
    jogador = int(input('Digite um número de 0 a 10: '))
    if jogador != maquina and 10 >= jogador >= 0:
        print('Você PERDEU!, você escolheu {} e a máquina {}\nTente novamente!'.format(jogador, maquina))
print('\n*********PARABÉNS*********\n')
print('Você GANHOU!, você escolheu {} e a máquina {}\n'.format(jogador, maquina))

