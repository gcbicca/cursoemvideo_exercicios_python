"""
Faça um programa que tenha uma FUNÇÃO chamada ÁREA(), que receba as dimensões de um terreno retangular
(LARGURA e COMPRIMENTO) e mostre a ÁREA DO TERRENO.
"""


# Essa função irá receber dois parâmetros área e comprimento e irá mostrar a área do terreno.

def area(largura, comprimento):
    """Essa função recebe 2 parâmetros largura e comprimento e exibe o área do terreno"""
    area_total = largura * comprimento
    print(f'A área de um terreno de {largura}x{comprimento} é de {area_total}m².')


# Irá pedir para o usuário inserir os dados do terreno
print(f'   CONTROLE DE TERRENOS')
print('=-'*20)
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
area(largura, comprimento)



