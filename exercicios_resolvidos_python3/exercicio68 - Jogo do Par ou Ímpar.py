"""
Faça um programa que jogue PAR ou ÍMPAR com o computador. O jogo só será
interrompido quando o jogador PERDER, mostrando o total de vitórias
consecutivas que ele conquistou no final do jogo.
"""

"""
n_int = int(input('Digite um número inteiro: '))
n_par_impar = n_int % 2
if n_par_impar == 0:
    print('O número inteiro {} é PAR'.format(n_int))
else:
    print('O número inteiro {} é ÍMPAR'.format(n_int))
from random import randint
from time import sleep
embaralha = randint(0, 5)
"""
import random
cont = win = 0
while True:
    cpu = random.randint(0, 10)
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Digite [PAR] ou [IMPAR]: ')).upper().strip()[0]
    player = int(input('Digite um número de 0 a 10: '))
    soma = cpu + player
    if soma % 2 == 0:
        result = 'P'
        if result == escolha:
            win += 1
            cont += 1
            print(f'Você venceu! Você escolheu PAR e {cpu} + {player} = {soma} e {soma} é PAR!')
        elif result != escolha:
            cont += 1
            print(f'Você perdeu! Você escolheu ÍMPAR e {cpu} + {player} = {soma} e {soma} é PAR!')
            print(f'Você venceu {win} vezes.')
            break
    elif soma % 2 != 0:
        result = 'I'
        if result == escolha:
            win += 1
            cont += 1
            print(f'Você venceu! Você escolheu ÍMPAR e {cpu} + {player} = {soma} e {soma} é ÍMPAR!')
        elif result != escolha:
            cont += 1
            print(f'Você perdeu! Você escolheu ÍMPAR e {cpu} + {player} = {soma} e {soma} é PAR!')
            print(f'Você venceu {win} vezes.')
            break
print('Acabou')