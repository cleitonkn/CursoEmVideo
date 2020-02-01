nome = str(input('Digite o seu nome completo: ')).strip()
nse = nome.split()
length = len(nome) - (nome.count(' '))

print(nome.upper())
print(nome.lower())
print('seu nome completo tem {} letras'.format(length))
# print('seu nome completo tem {} letras'.format(len(nome) - nome.count(' ')))
print('{} tem {} letras'.format(nse[0], len(nse[0])))
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))

