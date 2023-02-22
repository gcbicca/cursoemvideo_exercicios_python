""" Escreva um programa que leia DOIS NÚMEROS inteiros
e compare-os, mostrando na tela uma mensagem:
O PRIMEIRO VALOR é MAIOR
O SEGUNDO VALOR é MAIOR
NÃO EXISTE valor maior, os dois são IGUAIS
"""
n1 = int(input('Digite o primeiro número inteiro: '))
n2 = int(input('Digite o segundo número inteiro: '))
if n1 > n2:
    print(f'O número {n1} é maioor que o número {n2}.')
elif n2 > n1:
    print(f'O número {n2} é maior que o número {n1}.')
else:
    print(f'Náo existe valor maior, os os número {n1} e {n2} são iguais.')