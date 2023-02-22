"""
Desenvolva um programa que leia QUATRO VALORES pelo TECLADO e guarde-os em uma TUPLA. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números PARES.
"""
dados = (int(input('Digite um valor: ')), int(input('Digite outro valor: ')), int(input('Digite mais um valor: ')),
         int(input('Digite o último valor: ')))
pares = []
for c in dados:
    if c % 2 == 0:
        pares = pares + [c]# Ou só printa C com end= ' '
print(f'Os valores digitados foram: {dados}')
print(f'O número de vezes que apareceu o valor 9 é {dados.count(9)}')#Count conta quantas vezes apareceu o valor dentro de um variável
if 3 in dados:
    print(f'O número 3 foi digitado pela primeira vez na {dados.index(3)+1}ª posição')#Index mostra em que posicão apareceu pela primeira vez o valor determinado
else:
    print('O número 3 não foi digitado')
print(f'Os números pares são: {pares}')

#SOLUÇÃO != PARA OS PARES
print(f'O número pares são', end=' ')
for c in dados:
    if c % 2 == 0:
        print(c, end=' ')