'''Faça um programa que leia um número qualquer e mostre o seu fatorial.

ex:
5! = 5x4x3x2x1= 120'''

'''count = 1
num = int(input('Digite um número inteiro para descobir o seu fatorial: '))
print('{}! = {}x'.format(num, num), end='')
while count < num:
    n_num = num
    for c in range(num-1,0,-1):
        n_num = n_num * c
        print('{}x'.format(c), end='')
        count += 1
print('={}'.format(n_num))'''

'''from math import factorial
n = int(input('Digite um número para calcular seu fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}'.format(n, f))'''


num = int(input('Digite um número inteiro para descobir o seu fatorial: '))
c = num
f = 1
print('{}! = '.format(num), end='')
while c > 0:
        print('{}'.format(c), end='')
        print(' x ' if c > 1 else ' = ', end='')
        f *= c
        c -= 1
print('{}'.format(f))

