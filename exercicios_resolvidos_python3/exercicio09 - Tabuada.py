#Faça um programa que leia um numero inteiro qualquer e mostre na tela a sua tabuada
x = int(input('Digite um número inteiro: '))
print('A tabuada do {} é:'.format(x))
for y in range(1,11):
    tabuada = x * y
    print('{} x {:2} = {}'.format(x,y,tabuada))
