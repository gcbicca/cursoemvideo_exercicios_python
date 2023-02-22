"""
Crie um programa que vai gerar CINCO NÚMEROS ALEATÓRIOS e colocar um uma TUPLA.

Depois disso, mostre a LISTAGEM DE NÚMEROS gerados e também indique o MENOR e o MAIOR valor que estão na tupla.
"""
import random
cont = 0
lista = [ ]
while cont < 5:
    cont = cont + 1
    cpu = random.randint(0,1000)
    print(f'{cpu}')
    lista.append(cpu)
print(lista)
print(f'O maior valor da lista é {max(lista, key=int)}')
print(f'O menor valor da lista é {min(lista)}')
