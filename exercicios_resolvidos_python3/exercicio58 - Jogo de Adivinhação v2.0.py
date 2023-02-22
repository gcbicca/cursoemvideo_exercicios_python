'''
Melhore o jogo do DESAFIO 28 onde o computador vai "pensar"
em um NÚMERO ENTRE 0 E 10. Só que agora o jogador vai tentar
advinhar até acertar, mostrando no final quantos palpites
forma necessários para vencer.
'''
from random import randint
from time import sleep
cpu = randint(0, 10)
contador = 1
print('Olá! Sou seu computador.')
sleep(1)
print('Acabei de pensar em um número!')
sleep(2)
print('Para facilitar para você ele é de 0 a 10!')
sleep(2)
print('Será que você consegue adivinhar?')
sleep(2)
palpite = int(input('Digite o seu palpite: '))
if palpite != cpu:
    print('Você errou tente novamente!')
while cpu != palpite:
    palpite = int(input('Digite outro palpite: '))
    contador += 1
    if palpite < cpu:
        print('Você errou! Tente um número maior!')
    elif palpite > cpu:
        print('Você errou! Tente um número menor!')
print(f'Parabéns você acertou!\nO valor sorteado é {cpu}.'
      f'\nVocê tentou {contador}x.')

'''
acertou = False
while not acertou:
if jogador == computador:
    acertou = True
'''