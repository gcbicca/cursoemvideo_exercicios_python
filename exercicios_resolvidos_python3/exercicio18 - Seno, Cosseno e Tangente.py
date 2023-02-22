import math
'''Necessito converter os valores do ângulo tan(x) da formula da tan,sin e cos, pois o valor exibido
é dado em radianos e necessito em graus. Para isso utiliza-se a função
math.radians que converte ângulo em graus para radianos '''
tan = math.tan(math.radians(45))
sen = math.sin(math.radians(30))
print('A tangente é {:.2f}, o seno é {:.2f}'.format(tan, sen))
'''
#Faça um programa que leia um ãngulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ãngulo.
#MACETE: SENO COSSENO E TANGENTE, CO,CA,CO/CA, H, H RESULTANDO EM SENO:CO/H, COSSENO:CA/H, TANGENTE: CO/CA
import math
from typing import SupportsFloat

angulo = float(input('Digite o valor do ângulo: '))
seno = math.sin(angulo)
cosseno = math.cos(angulo)
tangente = math.tan(angulo)
print('O ângulo {}°, possui um seno de {}, cosseno {} e tangente {}'.format(angulo, seno, cosseno, tangente))
'''
