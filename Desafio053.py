# Crie um programa que leia uma frase qualquer e diga se ela é um palindromo,
# desconsiderando os espaços.

inicio = 0
countrever = 0
frase = str(input('Digite uma frase para identificarmos se ela é um palindromo: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
#inverso = ''
inverso = junto[::-1]
#for letra in range(len(junto) -1, -1, -1):
 #   inverso += junto[letra]
print(junto, inverso)

if junto == inverso:
    print('A frase escrita É UM palindromo!')
else:
    print('A frase escrita NÃO É UM palindromo!')

