# faça um programa que leia três números
# e mostre qual é o maior e qual é o menor.

n1 = int(input('Digite o primeiro numero inteiro: '))
n2 = int(input('Digite o segundo numero inteiro: '))
n3 = int(input('Digite o terceiro numero inteiro: '))

if n1 > n2 and n1 > n3:
    print('{} é o maior número'.format(n1))
if n2 > n1 and n2 > n3:
    print('{} é o maior número'.format(n2))
if n3 > n1 and n3 > n2:
    print('{} é o maior número'.format(n3))
if n1 < n2 and n1 < n3:
    print('{} é o menor número'.format(n1))
if n2 < n1 and n2 < n3:
    print('{} é o menor número'.format(n2))
if n3 < n1 and n3 < n2:
    print('{} é o menor número'.format(n3))