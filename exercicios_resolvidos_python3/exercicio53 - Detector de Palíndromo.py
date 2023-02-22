""" Crie um prgrama que leia uma FRASE qualquer e diga se ela é um PALÍNDROMO,
 desconsiderando os espaços.
"""
from time import sleep
'PALÍNDROMOS são frases que podem ser lidas de trás para frente. ex: Ana, ROMA ME TEM AMOR,APOS A SOPA'
frase = str(input('Digite um frase que deseje verificar se é um PALÍNDROMO: ')).strip().upper()# Tira espaços início e final

'''frase = frase.upper()''' #POSSO COLOCAR DO LADO DO .strip()

'''for s in frase:
    frase.join()
    frase.reverse()
    print(s)'''

separa = frase.split() #Separa a string por espaços e colooca em uma lista
junta = ''.join(separa) #''.join(lista qualquer) junta tudo com o caractere que quiser pode ser 'nada'
inverso = ''

#Forma diferente de inverter sem usar um laço
'inverso = junta[::-1]'

for letra in range(len(junta)-1, -1, -1): #len(junta) = 20 -1 = 19 até -1 que é antes da primeira, na ordem reversa.
    'print(junta[letra])#imprime a string letra por letra'
    inverso = inverso + junta[letra]# o inverso serve como um contador que vai acumulando as letras formando a palavra
print(f'A frase que você escreveu sem espaços fica:'
      f'\n\033[1;36m{junta}\033[m.'
      f'\nComparando com a mesma frase sem espaços e de trás para frente:'
      f'\n\033[1;33m{inverso}\033[m.'
      f'\nPortanto...')
sleep(2)
if junta == inverso:
    print('\033[1;35mA frase é um Palíndromo!\033[m')
else:
    print('\033[1;31mA frase não é um Palíndromo!')

