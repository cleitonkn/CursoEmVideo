nome = input('Digite o seu nome completo: ')
p_nome = nome.find(' ')
u_nome = nome.rfind(' ')
print('Seu primeiro nome é: {}'.format(nome[0:p_nome]))
print('Seu ultimo nome é: {}'.format(nome[u_nome+1:]))

