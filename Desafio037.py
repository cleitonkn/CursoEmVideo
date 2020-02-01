# Escreva um programa que leia um número inteiro qualquer e peça para o
# usuário escolher qual será a base de conversão:

# 1 para binário
# 2 para octal
# 3 para hexadecimal

print('-'*50)
print('Bem vindo ao conversor de valores')
print('-'*50)
dec = int(input('Digite um numero decimal inteiro no qual deseja converter:'))
print('Escolha uma das opções abaixo: ')
print('\n[1] - Para converter de decimal para binário')
print('\n[2] - Para converter de decimal para octal')
print('\n[3] - Para converter de decimal para hexadecimal')
print('-'*50)
opt = int(input('Sua opção: '))
print('-'*50)
if opt == 1:
    print('{} convertido para BINARIO é igual a {}'.format(dec, bin(dec)))
elif opt == 2:
    print(print('{} convertido para OCTAL é igual a {}'.format(dec, oct(dec))))
elif opt == 3:
    print(print('{} convertido para OCTAL é igual a {}'.format(dec, hex(dec))))
else:
    print('Opção invalida! tente novamente.')