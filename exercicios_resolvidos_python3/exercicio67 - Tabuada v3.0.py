"""
Faça um programa que mostre a TABUADA de VÁRIOS NÚMEROS,
um de cada vez, para cada valor digitado pelo usuário.
O programa será INTERROMPIDO quando o número solicitado for
NEGATIVO.
"""

"""y = int(input('Digite o número que deseja ver a tabuada: '))
print(f'O número escolhido foi {y}')
for x in range(1,11):
    print(f'{x:2} X {y} = {x * y}') #:2 cria espaços no inicio e nesse programa alinha os"""

while True:
    n = int(input('Digite um número inteiro para ver a tabuada (Digite um número negativo para interromper o programa): '))
    if n < 0:
        break
    for x in range(1, 11): #Do 1 ao 10 pois o range exclui o último número.
        print(f'{x:2} X {n} = {x * n}')
print('Programa da Tabuada ENCERRADO. Volte sempre!')