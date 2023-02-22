"""
Crie um programa que crie uma MATRIZ de DIMENSÃO 3X3 e preencha com valores
lidos pelo teclado. No final mostre a MATRIZ na tela, com a formatação correta.
"""
matriz = [[], [], []]
for c in range(0, 3):
    val = int(input(f'Digite um valor para [0, {c}]: '))
    matriz[0].append(val)
for c in range(0, 3):
    val = int(input(f'Digite um valor para [1, {c}]: '))
    matriz[1].append(val)
for c in range(0, 3):
    val = int(input(f'Digite um valor para [2, {c}]: '))
    matriz[2].append(val)
for l in range(0, 3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end=' ')
    print()
