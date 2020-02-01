import random

p = str(input('Digite o nome do primeiro aluno: '))
s = str(input('Digite o nome do segundo aluno: '))
t = str(input('Digite o nome do terceiro aluno: '))
q = str(input('Digite o nome do quarto aluno: '))

deck = [p, s, t, q]
random.shuffle(deck)
print(deck)




