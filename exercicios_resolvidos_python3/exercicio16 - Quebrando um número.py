#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
#Ex: Digite um número:24.5. O número 24.5 tem a parte inteira 24
import math
n1 = float(input('Digite um número: '))
print('O número {} tem a parte Inteira {}'.format(n1, math.trunc(n1)))
