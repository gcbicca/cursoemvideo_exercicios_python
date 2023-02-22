from random import randint
from operator import itemgetter
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
ranking = []
print('Valores sorteados: ')
for k, v in jogo.items():
    print(f'{k} tirou {v}')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)#Me retornou uma lista com tuplas
for i, v in enumerate(ranking):#tratar o ranking como uma lista
    print(f'{i+1} lugar: {v[0]} tirou {v[1]}')
print(ranking)