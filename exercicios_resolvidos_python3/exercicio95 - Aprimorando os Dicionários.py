"""
(93)Crie um programa que gerencie o aproveitamento de um JOGADOR DE FUTEBOL. O programa vai ler o NOME DO JOGADOR
e QUANTAS PARTIDAS ele jogou. Depois vai ler a QUANTIDADE DE GOLS feitos em CADA PARTIDA. No final, tudo isso
será guardado em um DICIONÁRIO, incluindo o TOTAL DE GOLS feitos durante o campeonato.
aproveitamento será uma lista.

(95)Aprimore o DESAFIO 093 para que ele funcione com VÁRIOS JOGADORES, incluindo um sistema de visualização
de DETALHES DO APROVEITAMENTO de cada jogador.
"""
dataset = []
while True:
    temp = {}
    temp['nome'] = str(input('Nome do jogador: ')).strip().title()
    temp['npartidas'] = int(input(f'Digite quantos jogos {temp["nome"]} jogou: '))
    temp['ngols'] = []
    for c in range(0,temp['npartidas']):
        temp['ngols'].append(int(input(f'Digite quantos gols {temp["nome"]} fez na partida {c}: ')))
    dataset.append(temp.copy())
    temp.clear()
    flag = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if flag in 'N':
        break
    print('--' * 30)
print('-=' * 30)
print(f'{"Cod.":<4} {"Nome":<15}{"Gols":<15} {"Total":>5}')
print('--' *30)
for i, l in enumerate(dataset):
    print(f"{i:<4} {dataset[i]['nome']:<15}{dataset[i]['ngols']}{sum(dataset[i]['ngols']):>10}")
    print('--'*30)
while True:
    flag2 = int(input('Mostrar dados de qual jogador?[STOP=999] '))
    if flag2 == 999:
        break
    if flag2 <= (len(dataset)-1):
        print(f'-- LEVANTAMENTO DO JOGADOR {dataset[flag2]["nome"]}:')
        for i, l in enumerate(dataset[flag2]['ngols']):
            print(f'    No jogo {i} fez {l} gols.')
        print('--' * 30)
    else:
        print(f'ERRO! Não existe jogador com código {flag2}! Tente novamente.')
print(dataset)