import random
p = input('Digite o nome do primeiro aluno: ')
s = input('Digite o nome do segundo aluno: ')
t = input('Digite o nome do terceiro aluno: ')
q = input('Digite o nome do quarto aluno: ')

print('\nO nome do aluno escolhido é {}: '.format(random.choice([p, s, t, q])))