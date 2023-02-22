#Faça um programa que leia três números e mostre qual é o MAIOR e qual é o MENOR.
n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
n3 = float(input('Digite o último número: '))
if n1 > n3 and n1 > n2:
    print('O número {} é o maior entre eles'.format(n1))
elif n1 < n2 and n1 < n3:
    print('O número {} é o menor entre eles'.format(n1))
else:
    print('O número {} não é o maior e nem o menor entre eles'.format(n1))
if n2 > n1 and n2 > n3:
    print('O número {} é o maior entre eles'.format(n2))
elif n2 < n3 and n2 < n1:
    print('O número {} é o menor entre eles'.format(n2))
else:
    print('O número {} não é o maior e nem o menor entre eles'.format(n2))
if n3 > n2 and n3 > n1:
    print('O número {} é o maior entre eles'.format(n3))
elif n3 < n1 and n3 < n2:
    print('O número {} é o menor entre eles'.format(n3))
else:
    print('O número {} não é nem o maior e nem o menor entre eles'.format(n3))
