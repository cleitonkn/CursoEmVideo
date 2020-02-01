# Faça um programa que calcule a soma entre todos os números impares
# que são multiplos de três e que se encontram no intervalo de 1 até 500.

soma = 0
cont = 0

print('Números pares no intervalo de 1 a 500:\n')
for a in range(1, 501):
    if a % 3 == 0:
       soma = a + soma
       cont = cont + 1
print(cont, soma)