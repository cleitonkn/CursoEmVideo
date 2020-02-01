# Escreva um programa que leia a velocidade
# de um carro.
# se ele ultrapassar 80Km/h, mostre uma
# mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km
# acima do limite.

vel = int(input('A qual velocidade que você se encontra: '))
print('Você ultrapassou o limite de 80Km/h e valor da multa é de R${:.2f}'.format((vel - 80)*7) if vel > 80 else 'Você esta dentro da velocidade permitida')