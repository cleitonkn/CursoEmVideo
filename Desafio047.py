# Crie um programa que mostre na tela todos os numeros pares que estão no
# intervalo entre 1 e 50.

print('Números pares no intervalo de 1 a 50:\n')
for a in range(1, 51):
    if a % 2 == 0:
        print(a)
