# Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar
# que tipo de triângulo será formado:
# - Equilatero: Todos os lados iguais
# - Isósceles: dois lados iguais
# - Escaleno: todos os lados diferentes

a = int(input('Digite o valor do lado "a" do triângulo: '))
b = int(input('Digite o valor do lado "b" do triângulo: '))
c = int(input('Digite o valor do lado "c" do triângulo: '))

if abs(b - c) < a < b + c and abs(a - c) < b < a + c and abs(a - b) < c < a + b:
    print('As medidas de a, b e c PODEM formar um triângulo')

    if a == b == c:
        print('O triangulo formado é um triângulo Equilatero')

    elif a == b or a == c or b == c:
        print('O triangulo formado é um triângulo Isósceles')

    elif a != b and a != c and b != c:
#   elif a != b != c != a (tambem funciona)
        print('O triangulo formado é um triângulo Escaleno')
else:
    print('As medidas de a, b e c NÂO PODEM formar um triângulo')



