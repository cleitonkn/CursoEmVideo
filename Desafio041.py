# a confederação nacional de natação precisa de um programa que leia o
# ano de nascimento de um atleta e mostre sua categoria, de acordo com a
# idade:

# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JUNIOR
# - Até 25 anos: SENIOR
# - Acima: Master

from datetime import date

atual = date.today().year
nasc = int(input('\nDigite o ano do seu nascimento: '))

ano = atual - nasc

if ano <= 9:
    print('\nVocê tem {} anos e faz parte da categoria MIRIM.'.format(ano))
elif ano <= 14:
    print('\nVocê tem {} anos e faz parte da categoria INFANTIL.'.format(ano))
elif ano <= 19:
    print('\nVocê tem {} anos e faz parte da categoria JUNIOR.'.format(ano))
elif ano <= 25:
    print('\nVocê tem {} anos e faz parte da categoria SENIOR'.format(ano))
elif ano > 25:
    print('\nVocê tem {} anos e faz parte da categoria MASTER'.format(ano))