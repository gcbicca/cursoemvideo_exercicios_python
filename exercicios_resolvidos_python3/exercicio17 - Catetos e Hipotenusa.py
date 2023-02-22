'''co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hipotenusa = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))'''
import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hipotenusa = math.hypot(co,ca)# Função math.hypot calcula a hipotenusa só precisa colocar os valores do cateto oposto e do cateto adjacente.
print('O valor da hipotenusa é {:.2f}'.format(hipotenusa))
'''
#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
import math
cateto_oposto = float(input('Digite o valor do cateto oposto: '))
cateto_adjacente = float(input('Digite o valor do cateto adjacente: '))
hipotenusa_quadrada = (cateto_adjacente**2) + (cateto_oposto**2)
hipotenusa = math.sqrt(hipotenusa_quadrada)
print('Considerando que o triangulo é um triângulo retângulo, a hipotenusa ao quadrado é o cateto oposto a alpha ao quadrado {}² mais o cateto adjacente a alpha ao quadrado {}² resultando em: {}'.format(cateto_oposto, cateto_adjacente,hipotenusa))

'''
