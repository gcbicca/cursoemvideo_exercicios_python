from random import randint
from time import sleep
lista = []
jogos = []
xjogos = 1
print(f'~' * 40)
print('      JOGOS DA MEGA SENA         ')
print(f'~' * 40)
numjogos = int(input('Digite quantos jogos serão gerados: '))
while xjogos <= numjogos:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    xjogos += 1
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
print(f'-=' * 3, f'SORTEANDO {numjogos} JOGOS', '-=' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('-=' * 5, f'< BOA SORTE! >', '-=' * 5)
