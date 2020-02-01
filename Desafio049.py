# Refaça o desafio 009, mostrando a tabuada de um número que o usuário
# escolher, só que agora utilizando um laço for.

a = int(input('Digite um número inteiro para descobrir a sua tabuada: '))
print('\nA tabuada do número {} é: \n'.format(a))

for c in range(0,11):
    print('{} x {} = {}'.format(a, c, a*c))