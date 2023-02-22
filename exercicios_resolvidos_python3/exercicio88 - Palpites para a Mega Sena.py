"""
Faça um programa que ajude um jogador da MEGA SENA a criar PALPITES. O programa
vai perguntar QUANTOS JOGOS serão gerados e vai sortear 6 NÚMEROS ENTRE 1 E 60
para cada jogo, cadastrando tudo em uma LISTA COMPOSTA.
"""
from random import randint
lista = []
njogos = int(input('Digite quantos jogos serão gerados: '))
for c in range(0, njogos):
        lista.append([randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60)])
for c in range(0, njogos):
    lista[c].sort()
temp = 0
for l in range(0, njogos):
    for pos, value in enumerate(lista[l]):
        if temp == value:
            lista[l][pos-1] = randint(1, 60)
            for c in range(0, njogos):
                lista[c].sort()
        temp = value
print(lista)
