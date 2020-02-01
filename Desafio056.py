from math import ceil
p_idade = 0
soma = 0
count = 0
nome_hv = str
for c in range(0, 4):
    print('-----{}° PESSOA_-----'.format(c+1))
    #print('Dados do usuário número {}°'.format(c+1))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()
    soma += idade
    if idade > p_idade and sexo == 'M':
        nome_hv = nome
        p_idade = idade
    elif sexo == 'F' and idade <= 20:
        count = count+1
print('\nA média de idade é igual a {} anos.'.format(soma/4))
print('O nome do homem mais velho é {} com {} anos.'.format(nome_hv,p_idade))
print('Há {} mulheres com idade menor que 20 anos.'.format(ceil(count)))

# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.no
# final do programa, mostre:

# - A media de idade do grupo
# - Qual é o nome do homem mais velho
# - Quantas mulheres tem menos de 20 anos.