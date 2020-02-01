# Faça um programa que leia o ano de nascimento um jovem e informe,
# de acordo com a sua idade:
# - Se ele ainda vai se alistar ao serviço militar
# - Se é a hora de se alistar.
# - Se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo
from datetime import date

atual = date.today().year
nasc = int(input('En que ano você nasceu: '))

ano = atual - nasc
print ('Quem nasceu em {} tem {} anos'.format(nasc, ano))

if ano == 18:
    print('Você tem até o dia 30/06/2020 para se alistar!')
elif ano < 18:
    print('Ainda faltam {} anos para o alistamento militar'.format(ano-18))
else:
    print ('Você tem mais de 18 anos! Você já não se enquadra mais no alistamento obrigatorio.')