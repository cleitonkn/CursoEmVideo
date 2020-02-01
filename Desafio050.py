# Desenvolva um programa que leia seis números inteiros e mostre a some
# apenas daqueles que forem pares. Se o valor digitado for impar desconsidere-o.

soma = 0
cont = 0
for a in range(1, 7):
    n = int(input('Digite o {}° número inteiro: '.format(a)))
    if n % 2 == 0:
       cont += 1
       soma += n
print('Você informou {} numeros pares e a  soma foi {}'.format(cont, soma))