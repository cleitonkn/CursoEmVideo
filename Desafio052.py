num = int(input('Digite um número inteiro para descobrir se o mesmo é um número primo: '))
cont = 0
for c in range(1, num+1):
    if num % c == 0:
        print('\033[33m', end=' ')
        cont += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
if cont > 2:
    primo = 'NÂO É PRIMO'
else:
    primo = 'É PRIMO'
print('\033[0:30m\nO número {} foi divisível {} vezes\ne por isso ele {}'.format(num, cont, primo))
# Faça um programa que leia um numero inteiro
# e diga que se ele é ou não um numero primo.