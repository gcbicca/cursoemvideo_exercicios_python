"""Faça um programa que tenha uma LISTA chamada NÚMEROS e duas FUNÇõES chamdas SORTEIO() e
SOMAPAR(). A primeira função vai sortear 5 NÚMEROS e vai colocá-los dentro da lista e a segunda função vai mostrar
a SOMA entre todos os valores PARES sorteados pela função anterior."""
from random import randint
# Definindo uma lista vazia
numeros_sorteados = []
numeros_sorteados2 = []


# Essa função irá sortear 5 números e coloca-os dentro de uma lista.
def sorteio():
    """Essa função sorteia 5 números e coloca-os dentro de uma lista"""
    c = 0
    while c < 5:
        num_sorteado = randint(0, 50)
        numeros_sorteados.append(num_sorteado)
        c += 1
    for cont in range(0, 5):
        num_sorteado2 = randint(0, 50)
        numeros_sorteados2.append(num_sorteado2)


sorteio()
print(f'Os números sorteados foram:', end=' ')
for c in numeros_sorteados:
    print(f'{c}', end=' ')
print('.')
print(numeros_sorteados2)


# Essa função irá somar os valores pares entre todos os valores na lista.
def somarpar():
    """Essa função irá somar os valores pares da lista de valores"""
    print(f'Somando os valores pares de: {numeros_sorteados}. Temos ', end='')
    tot = 0
    for v in numeros_sorteados:
        if v % 2 == 0:
            tot = tot + v
    print(tot, '.')

    
somarpar()