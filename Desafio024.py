# crie um programa que leia o nome de uma cidade e diga se ela começa
#ou não com o nome "SANTO".

# primeiro modo ( Curso em video)
cid = str(input('Em que cidade você nasceu? ')).strip()
print(cid[:5].upper() == 'SANTO')

# segundo modo ( Meu)
a = str(input('Digite o nome da sua cidade: ')).strip()
b = a.upper()
c = b.split()
print('Sua cidade começa com a palavra SANTO? {}'.format('SANTO' in c))
