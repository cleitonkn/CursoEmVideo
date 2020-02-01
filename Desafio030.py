# Crie um programa que leia um número
# inteiro e mostre na tela se ele é
# PAR ou IMPAR.

n = int(input('Digite um número inteiro qualquer: '))
print('O numero {} é PAR'.format(n) if n%2 == 0 else 'O numero {} é IMPAR'.format(n))