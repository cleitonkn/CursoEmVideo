# faça um programa que leia uma frase pelo teclado e mostre:
# a) quantas vezes aparece a letra "A".
# Em que posição ela aparece a primeira vez.
# Em que posição ela aparece a ultima vez.

frase = str(input('Escreva uma frase qualquer: ')).strip().lower()
print(' A letra "a" foi encontrada na frase {} vezes'.format(frase.count('a')))
print(' A letra "a" foi encontrada a primeira vez na posição {}'.format(frase.find('a')+1))
print(' A letra "a" foi encontrada a ultima vez na posição {}'.format(frase.rfind('a')+1))