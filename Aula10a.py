# Estruturas condicionais
# Curso Python - condicões simples e compostas
# Estrutura sequencial =/ estrutura condicional

tempo = int(input('Quantos anos tem seu carro? '))
if tempo <=3:
    print('Carro novo')
else:
    print('Carro velho')

print('--FIM--')

# Estrutura condicional simples
nome = str(input('Qual é o seu nome? ')).lower()
if nome == 'gustavo':
    print('Que nome lindo você tem!')
print('Bom dia {}!.'.format(nome))

# Estrutura condicional composta
nome2 = str(input('Qual é o seu nome? ')).lower()
if nome2 == 'gustavo':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')
print('Bom dia {}!.'.format(nome2))

# Estrutura condicional simplificada
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('A sua média foi {:.1f}'.format(m))
print('PARABÉNS' if m>=6 else 'ESTUDE MAIS!')

