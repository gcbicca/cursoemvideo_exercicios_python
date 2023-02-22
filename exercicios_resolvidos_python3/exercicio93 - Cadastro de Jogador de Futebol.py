"""
Crie um programa que gerencie o aproveitamento de um JOGADOR DE FUTEBOL. O programa vai ler o NOME DO JOGADOR
e QUANTAS PARTIDAS ele jogou. Depois vai ler a QUANTIDADE DE GOLS feitos em CADA PARTIDA. No final, tudo isso
será guardado em um DICIONÁRIO, incluindo o TOTAL DE GOLS feitos durante o campeonato.
aproveitamento será uma lista
"""
dataset = {}
dataset['name'] = str(input('Players name: ')).strip().title()
dataset['nmatches'] = int(input(f'Number of matches did {dataset["name"]} play: '))
dataset['goals'] = []
for c in range(0, dataset['nmatches']):
    dataset['goals'].append(int(input(f'Number of goals of match {c+1}: ')))
"""total_goals = 0
for goals in dataset['goals']:
    total_goals += goals"""
dataset['total'] = sum(dataset['goals'])
print('=-' * 30)
print(dataset)
print('=-' * 30)
for k, v in dataset.items():
    print(f'The field {k} have the value {v}.')
print('=-' * 30)
print(f'The player {dataset["name"]} played {dataset["nmatches"]} matches.')
for i, v in enumerate(dataset['goals']):
    print(f'   => In the match {i+1}, done {v} goals')
print(f'Was been a total of {dataset["total"]} goals.')