# Desenvolva um programa que leia o
# comprimento de três retas e diga ao
# usuario se elas podem ou não formar
# um triângulo.

a = int(input('Digite o valor do lado "a" do triângulo: '))
b = int(input('Digite o valor do lado "b" do triângulo: '))
c = int(input('Digite o valor do lado "c" do triângulo: '))

if abs(b - c )< a < b + c and abs(a - c ) < b < a + c and abs(a - b )< c < a + b:
    print('As medidas de a, b e c PODEM formar um triângulo')
else:
    print('As medidas de a, b e c NÂO PODEM formar um triângulo')