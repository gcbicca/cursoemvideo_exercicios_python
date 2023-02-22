""" Faça um programa que calcule a soma entre todas os
NÚMEROS ÍMPARES que são MÚLTIPLOS DE TRÊS  e que se encontram
no intervalo de 1 até 500."""
soma = 0
cont = 0
for c in range(0, 500, 3):# (1, 501, 3) (1, 501 , 2) (0, 500, 3)
    if c % 2 != 0: #if c % 3 == 0
        cont = cont + 1# += mesmo que a variavel mais ela mesma mais alguma coisa
        soma = c + soma# +=
print(f'A soma de todos os {cont} números resulta em {soma}.')