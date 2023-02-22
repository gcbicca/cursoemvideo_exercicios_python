"""
Crie um programa onde 4 JOGADORES joguem um DADO e tenham resultados aleatórios. Guarde
esses resultados em um DICIONÁRIO. No final, coloque esse dicionário em ORDEM, sabendo que o VENCEDOR tirou
o MAIOR NÚMERO no dado.
"""
from random import randint
from time import sleep
dataset = {}
for c in range(1, 5):
    dataset[f'jogador{c}'] = randint(1, 6)
print('Valores sorteados: ')
for k, v in dataset.items():
    print(f'{k} tirou {v} no dado')
    sleep(1)
print('-=' * 30)
print('    == RANKING DOS JOGADORES ==    ')
c = 0
for v in sorted(dataset, key=dataset.get, reverse=True):#v retorna o key com valores em ordem ('jogador4')
    c += 1
    print(f'{c}º Lugar: {v} com {dataset[v]}')
print(dataset)
