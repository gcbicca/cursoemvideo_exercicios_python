'''
Escreva um programa que faça o computador pensar em um número inteiro entre 0 e 5 e
peça para o usuário tentar descobrir qual foi o número escolhido pelo computador
O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''
from random import randint
from time import sleep
embaralha = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
palpite = int(input('Digite o seu palpite de um número entre 0 e 5: '))
print('PROCESSANDO...')
sleep(2)
if palpite == embaralha:
    print('Parabéns você acertou! O número sorteado foi {}'.format(embaralha))
else:
    print('OPS! Você errou! Tente denovo da próxima vez!')

