from random import sample
from time import sleep
jogos = []
n = int(input('Digite quantos jogoso serão gerados: '))
for c in range(0, n):
    num = sorted(sample(range(1, 61), 6))
    jogos.append(num[:])
    print(f'Jogo {c+1}:{num}')
    sleep(1)