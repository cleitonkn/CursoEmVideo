# Desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule
# seu IMC e mostre seu status, de acordo com a tabela abaixo:
# - Abaixo de 18.5: Abaixo do peso
# - Entre 18.5 e 25: Peso ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade mórbida

Peso = float(input('Digite o seu peso atual: '))
Altura = float(input('Digite a sua altura em metros: '))
IMC = Peso / (Altura**2)
print('Seu IMC é de {:.2f}'.format(IMC))

if IMC < 18.5:
    print('Você está abaixo do peso ideal')
elif 25 > IMC >= 18.5:
    print('Você está no seu peso ideal')
elif 30 > IMC >= 25:
    print('Você está com sobrepeso')
elif 40 > IMC >= 30:
    print('Você apresenta Obesidade')
else:
    print('Você apresenta Obesidade mórbida')