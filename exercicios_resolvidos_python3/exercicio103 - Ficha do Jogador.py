"""
Faça um programa que tenha uma FUNÇÃO chamada FICHA(), que receba dois PARÂMETROS OPCIONAIS: o NOME de um jogador e
quantos GOLS ele marcou.

O programa deverá ser capaz de mostrar a FICHA DO JOGADOR, mesmo que algum dado não tenha sido informado corretamente.
ex:
linha
input, nome do jogador # Se eu não inserir o nome e nem os gols
o jogador <desconhecido> fez 0 gol(s) no campeonato.
input, N de gols
print o jogador romario fez 33 gol(s) no campeonato.
"""


# Função receberá dois parâmetros opcionais, nome e gols
def ficha(nome='', gols=''):
    """
    -> Essa função irá exibir um nome de um jogador e quantos gols eles fez.
    :param nome: Insira o nome de um jogador.
    :param gols: Insira um número inteiro para o número de gols que o jogador fez
    :return: sem retorno
    """
    if not gols:
        gols = 0
    elif gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0
    if nome == '':
        print(f'O jogador <desconhecido> fez {gols} gol(s) no campeonato.')
    else:
        print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


# Programa principal
#name = str(input('Nome do jogador: ')).strip().title()
#goal = input('Número de gols: ').strip()
#ficha(name, goal)
ficha(str(input('Nome do jogador: ')).strip().title(), input('Número de gols: ').strip())
