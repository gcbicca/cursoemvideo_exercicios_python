"""
Aprimore o DESAFIO ANTERIOR, mostrando no final:
a) A SOMA de todos os VALORES PARES digitados.
b) A SOMA dos valores da TERCEIRA COLUNA.
c) O MAIOR valor da SEGUNDA LINHA.
"""
matriz = [[], [], []]
spares = ster = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l].append(int(input(f'Digite um valor para [{l}, {c}]: ')))
print(f'-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            spares = matriz[l][c] + spares
    print()
print(f'-=' * 30)
print(f'A soma dos valores pares é {spares}')
print(f'=-' * 30)
for l in range(0, 3):
    ster = matriz[l][2] + ster
print(f'O valor da soma dos valores da terceira coluna é: {ster}')
print(f'=-' * 30)
print(f'O maior valor da segunda coluna é {max(matriz[1])}')
