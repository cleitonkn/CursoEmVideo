# Crie um programa que leia duas notas de um aluno e calcule a sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÂO
# - Média 7.0 ou superior: APROVADO
print('-*'*20)
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('\nDigite a segunda nota: '))
m = (n1+n2)/2
print('-*'*20)
print('\nSua média foi de {}'.format(m))
if m < 5:
    print('Você foi reprovado!')
elif 7 > m >= 5:
     print('Você esta de RECUPERAÇÂO!')
elif m >= 7:
     print('Voce foi APROVADO!')
