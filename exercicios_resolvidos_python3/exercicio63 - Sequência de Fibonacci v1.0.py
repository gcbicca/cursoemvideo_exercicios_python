'''
Escreva um programa que leia um NÚMERO N inteiro qualquer e
mostre na tela a quatidade de elementos da SEQUÊNCIA DE
FIBONACCI = é uma sucessão de números que obedecem um padrão em que cada elemento subsequente é a soma dos dois anteriores
Ex:
0 → 1 → 1 → 2 → 3 → 5 → 8
'''
n = int(input('Digite quantos termos você quer da Sequência de Fibonacci: '))
nant = 1
fibonacci = 0
while n != 0:
    print(f'{fibonacci}', end=' → ')
    fibonacci = fibonacci + nant
    nant = fibonacci - nant
    n -= 1
print('Fim')
