largura = float(input('\nDigite a largura da parede em metros: '))
altura = float(input('Digite a sua altura em metros: '))

area = largura*altura
quant = area/2

print('\nSua parede possui {} metros quadrados e necessita de {} litros para que seja pintada'.format(area, quant))

