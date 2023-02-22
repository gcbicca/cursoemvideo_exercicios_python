""" Faça um programa que leia um NÚMERO INTEIRO e diga se ele é ou não um número primo."""
n = int(input('Digite um número inteiro: '))
'Número primos tem apenas 2 divisores'
cont = 0
for c in range(1, n+1):
    if n % c == 0:
        print(f'\033[1;36m{c}\033[m', end=' ')
        cont += 1
    else:
        print(f'\033[1;33m{c}\033[m', end=' ')
if cont != 2:
    print(f'\nO número {n} não é um número PRIMO, pois, pode ser divisível por {cont} números.')
elif cont == 2:
    print(f'\nO número {n} é um número PRIMO, pois, pode ser divisível por {cont} números.')