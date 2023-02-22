""" Escreva um programa que leia um número inteiro qualquer e peça para o usuário
escolher qual será a BASE DE CONVERSÃO:
1 para BINÁRIO
2 para OCTAL
3 para HEXADECIMAL
"""
num = int(input('Digite um número inteiro: '))
base_num = int(input('Digite um número de 1 a 3, sendo 1 para Binário, 2 para Octal e 3 para Hexadecimal: '))
if base_num == 1:
    print(f'O número {num} convertido para o sistema Binário fica: {bin(num)[2:]}')# o valor aparecerá uma tag ex: 0b1010 o "0b" representa número binário
elif base_num == 2:
    print(f'O número {num} convertido para o sistema Octal fica: {oct(num)[2:]}')
elif base_num ==3:
    print(f'O número {num} convertido para o sistema Hexadecimal fica: {hex(num)[2:].upper()}')
else:
    print('Opção inválida')

