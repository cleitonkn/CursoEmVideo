import random
# Escreva um programa que faça o computador
# pensar em um número inteiro entre 0 e 5 e
# peça para o usuário tentar descobrir
# Qual foi o número escolhido pelo computador.

# o programa deverá escrever na tela se o
# usuário venceu ou perdeu.

n1 = random.randint(0, 5)
n2 = int(input('Digite um número inteiro de 0 a 5: '))
if n1 == n2:
    print('Parabéns você ganhou!, o número escolhido pela maquina foi {} e o seu {}...'.format(n1, n2))
else:
    print('Não foi dessa vez! tente novamente o número escolhido pela maquina foi {}...'.format(n1))