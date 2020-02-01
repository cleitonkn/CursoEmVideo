''' faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "M"
ou "F". Casa esteja errado peça a digitação novamente até ter um valor correto.
'''

'''a = 0
while a == 0:
    sexo = str(input('\nQual o seu sexo? ')).strip().upper()
    if sexo == 'M' or sexo == 'F':
        a = 1
    else:
        print('O valor invalido!...\nDigite "M" para masculino e "F" para feminino.')
print('O valor digitado foi {}'.format(sexo))'''

sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper() [0]
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Por favor, informe o seu sexo: ')).strip().upper() [0]
print('Sexo {} registrado com sucesso'.format(sexo))

