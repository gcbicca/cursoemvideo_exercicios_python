"""
Crie um módulo chamado MOEDA.PY que tenha as funções incorporadas
AUMENTAR(), DIMINUIR(), DOBRO() E METADE().

Faça também um programa que IMPORTE esse módulo e use algumas dessas funções
ex:
from ex107 import moeda
p = float(input('Digite o preço: R$')
print(f'A medate de {p} é {moeda.metade(p)')
print(f'O dobro de {p} é {moeda.dobro(p)}')
print(f'O aumento de 10%, temos {moeda.aumentar(p, 10)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(p, 13)}')
"""
from Cursoemvideo_exercicios import moeda
#from Cursoemvideo_exercicios.modulos import moeda
preco = float(input('Digite um preço: R$'))
print(f'A metade de {moeda.moeda(preco)} é {moeda.moeda(moeda.metade(preco))}')
print(f'O dobro de {moeda.moeda(preco)} é {moeda.moeda(moeda.dobro(preco))}')
print(f'O aumento de 10% de {moeda.moeda(preco)} é {moeda.moeda(moeda.aumentar(preco, 10))}')
print(f'A redução de 13% de {moeda.moeda(preco)} é {moeda.moeda(moeda.diminuir(preco, 13))}')