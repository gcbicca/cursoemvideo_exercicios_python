"""
Faça um MINI-SISTEMA que utilize o INTERCTIVE HELP do PYTHON. O usuário vai digitar o COMANDO e o MANUAL vai aparecer.
Quando o usuário digitar a palavra 'FIM', o programa se encerrará.
OBS: use CORES.
ex:
linha
SITEMA DE AJUDA PyHELP
linha
Função ou biblioteca > len
linha
Acessando o manual do comando "len"
linha
(Manual do Len)
linha
SITEMA DE AJUDA PyHELP
linha
Função ou biblioteca > fim
linha
Até logo
linha
"""
from time import sleep


def print_bonito(txt, n_estilo, numero_cor, numero_fundo=0):
    tam = len(txt) + 4
    print(f'\033[{n_estilo};{numero_cor};{numero_fundo}m~' * tam)
    print(f'   {txt}')
    print('~' * tam, '\033[m')


while True:
    print_bonito('SISTEMA DE AJUDA PyHelp', 0, 30, 42)
    q = input('Função ou biblioteca > ').strip()
    if q.lower() == 'fim':
        break
    sleep(1)
    print_bonito(f'Acessando o manual do comando {q}', 0, 30, 44)
    sleep(1)
    print('\033[7:30m>')
    help(q)
