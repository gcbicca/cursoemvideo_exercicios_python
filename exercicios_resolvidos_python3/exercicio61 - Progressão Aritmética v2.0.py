"""
Refaça o DESAFIO 51, lendo o PRIMEIRO TERMO e a RAZÃO de uma
PA, mostrando os 10 PRIMEIROS TERMOS da progressão usando
a estrutura WHILE.
"""

a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da Progressão Aritmética: '))
c = 10
while c != 0:
    print(a1, end=' → ')
    a1 += r
    c -= 1
print('Fim')
