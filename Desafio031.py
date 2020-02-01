# Desenvolva um programa que pergunte
# a distância de uma viagem em km.
# calcule o preço da passagem. Cobrando
# R$0,50 por Km para viagens até 200Km
# e R$0,45 para viagens muito mais longas.

dist = float(input('Digite a distância até o destino em Km: '))
print('O valor da viagem será de {:.1f}*R$0,50 = R${:.2f}'.format(dist, dist*0.50) if dist <= 200 else 'O valor da viagem será de {:.1f}*R$0,45 = R${:.2f}'.format(dist, dist*0.45))