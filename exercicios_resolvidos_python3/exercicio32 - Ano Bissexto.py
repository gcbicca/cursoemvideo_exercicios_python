#Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
'''
Divisível por 4. Sendo assim, a divisão é exata com o resto igual a zero;
Não pode ser divisível por 100. Com isso, a divisão não é exata, ou seja, deixa resto diferente de zero;
Pode ser que seja divisível por 400. Caso seja divisível por 400, a divisão deve ser exata, deixando o resto igual a zero.
Terceira situação: Se o ano de 2015 ou 2016 não for divisível por 4, então devemos verificar se ele é divisível por 400. Caso seja, o ano de 2015 é bissexto.
'''
from datetime import date
ano_bi = int(input('Digite um ano qualquer. Coloque 0 para analisar o ano atual: '))
if ano_bi == 0:
    ano_bi = date.today().year
div_4 = ano_bi % 4 #Tem que ser divisivel por 4, resto 0
div_100 = ano_bi % 100#Não pode ser divisível por 100, resto >0
div_400 = ano_bi % 400#pode ser divisivel por 400, resto 0
if div_4 == 0 and div_100 > 0:
    print('O ano {} é um ano Bissexto'.format(ano_bi))
elif div_400 == 0:
    print('O ano {} é um ano Bissexto'.format(ano_bi))
else:
    print('O ano {} não é um ano Bissext0'.format(ano_bi))
#if ano_bi % 4 == 0 and ano_bi % 100 != 0 or ano_bi % 400 == 0:

