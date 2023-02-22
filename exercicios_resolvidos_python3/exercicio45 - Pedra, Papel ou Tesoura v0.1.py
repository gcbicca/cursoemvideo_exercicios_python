from random import randint
from time import sleep
formas = ('PEDRA', 'PAPEL', 'TESOURA')
cpu = randint(0, 2)
print('''Digite sua forma:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Opção: '))
if jogador != 0 and jogador != 1 and jogador !=2:
    print('\033[1;31mJogada inválida! Tente novamente com uma alternativa válida!\033[m')
    exit()
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
print('-='*20)
print(f'Você jogou: {formas[jogador]}')
print(f'O COMPUTADOR jogou: {formas[cpu]}')
print('-='*20)
if cpu == 0: #CPU escolheu PEDRA
    if jogador == 0: #Jogador escolheu PEDRA
        print('\033[1;33mEMPATE\033[m')
    elif jogador == 1:#Jogador escolheu PAPEL
        print('\033[1;36mVocê VENCEU! PAPEL cobre a PEDRA.\033[m')
    elif jogador == 2:#Jogador escolheu TESOURA
        print('\033[1;31mVocê PERDEU! PEDRA quebra a TESOURA.\033[m')
elif cpu == 1: #CPU escolheu PAPEL
    if jogador == 0:#Jogador escolheu PEDRA
        print('\033[1;31mVocê PERDEU! PAPEL cobre a PEDRA.\033[m')
    elif jogador == 1:#Jogador escolheu PAPEL
        print('\033[1;33mEMPATE\033[m')
    elif jogador == 2:#Jogador escolheu TESOURA
        print('\033[1:36mVocê VENCEU! TESOURA corta o PAPEL.\033[m')
elif cpu == 2:#CPU escolheu TESOURA
    if jogador == 0:#Jogador escolheu PEDRA
        print('\033[1;36mVocê VENCEU! PEDRA quebra a TESOURA.\033[m')
    elif jogador == 1:#Jogador escolheu PAPEL
        print('\033[1:31mVocê PERDEU! TESOURA corta o PAPEL.\033[m')
    elif jogador == 2:#Jogador escolheu TESOURA
        print('\033[1;33mEMPATE\033[m')
