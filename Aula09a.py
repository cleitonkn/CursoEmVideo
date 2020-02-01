frase = 'Curso em Video Python'
print(frase[1:15])

texto = ("""   Universo Online, conhecido pela 
sigla UOL, é uma empresa brasileira 
de conteúdo, produtos e serviços de 
Internet do conglomerado Grupo Folha. 
Em 2017, foi considerado pela plataforma
SimilarWeb o sexto site mais visitado 
da Internet no Brasil, atrás dos sites 
do Google e do Facebook.    """)

print(texto)
print('-'*40)
print(texto.count('o'))
print('-'*40)
print(texto.upper().count('O'))
print('-'*40)
print(len(texto))
print('-'*40)
print(texto.strip())
print('-'*40)
print(texto.replace('Google', 'Viado'))
print('-'*40)
print('Google' in texto)
print('-'*40)
print(texto.find('Uol'))
print('-'*40)
print(texto.lower().find('uol'))
print('-'*40)
print(frase.split())
print('-'*40)
dividido = frase.split()
print(dividido[2])
print('-'*40)
print(dividido[2][3])