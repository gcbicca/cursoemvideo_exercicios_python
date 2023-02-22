'''
Faça um programa que mostre na tela uma CONTAGEM REGRESSIVA para o estouro
de fogos de artifício, indo de 10 até 0, com uma pausa de 1 SEGUNDO entre eles.
'''
from time import sleep
for c in range (10, -1 ,-1): # o -1 serve para contar de trás para frente
    print(c)
    sleep(1)# da biblioteca time importa o sleep que dá uma pausa ao exibir o próximo valor
print('POOW!, BUM!, PUM!, PUM!, PUM!')
