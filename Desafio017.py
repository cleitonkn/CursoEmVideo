import math
co = float(input('\nDigite o comprimento do cateto oposto: '))
ca = float(input('\nDigite o comprimento do cateto adjacente: '))

print('\nO valor da hipotenusa é igual a {:.2f}'.format(math.hypot(ca, co)))