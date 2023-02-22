"""
Faça um programa que leia um número de 0 a 9999 e mostre na
tela cada um dos dígitos separados.
Ex:Digite um número:1834
Unidade:4
Dezena:3
Centena:8
Milhar:1
"""
'''
n = input('Digite um número entre 0 e 9999: '))
n_unidade = n[3]
print('Unidade:{}'.format(n_unidade))
n_dezena = n[2]
print('Dezena:{}'.format(n_dezena))
n_centena = n[1]
print('Centena:{}'.format(n_centena))
n_milhar = n[0]
print('Milhar:{}'.format(n_milhar))
Para realizar dessa forma necessita-se usar estruturas de repetição
entretanto pode-se realizar utilizando uma forma matemática
'''
'''
n = int(input('Digite um número de 0 a 9999: '))
n_str = str(n) #Converte o número inteiro inserido em string
print('O número digitado foi {}'.format(n))
print('Unidade:{}'.format(n[3]))
print('Dezena:{}'.format(n[2]))
print('Centena:{}'.format(n[1]))
print('Milhar:{}'.format(n[0]))
'''
n = int(input('Digite um número de 0 a 9999: '))
u = n // 1 % 10 #Se eu dividir 1234/10 = 123.4 se eu fizer o módulo sobrará 4
d = n // 10 % 10 #1234//10 = 123 ele come o .4 depois 123%10 = 3
c = n // 100 % 10 #1234//100 = 12 depois 12%10 = 2
m = n // 1000 % 10#1234//1000 = 1 depois 1%10 = 1 pois = 0.1 sobra 1
print('O número digitado foi {}'.format(n))
print('Unidade:{}'.format(u))
print('Dezena:{}'.format(d))
print('Centena:{}'.format(c))
print('Milhar:{}'.format(m))
