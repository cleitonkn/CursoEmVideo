# Faça um programa que leia um ano
# qualquer e mostre se ele é BISSEXTO.
from datetime import date


b = int(input('Digite um ano qualquer a partir de 1582 para se descobrir se o mesmo é bissexto: '))

if b == 0:
    b = date.today().year
if b % 4 == 0:
    print('O ano {} é um ano Bissexto'.format(b))
else:
    print ('O ano {} não é uma no Bissexto'.format(b))