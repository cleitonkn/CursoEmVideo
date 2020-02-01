# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual
# foi o o maior e menos peso lidos.
maior_peso = 0
menor_peso = 0
for a in range(0, 5):
    peso = float(input('Digite o {}° peso: '.format(a+1)))
    if peso > maior_peso:
        maior_peso = peso
    if a == 0 or peso < menor_peso:
        menor_peso = peso
        #count += 1
print('O maior peso é de {}Kg e o menor {}Kg'.format(maior_peso, menor_peso))