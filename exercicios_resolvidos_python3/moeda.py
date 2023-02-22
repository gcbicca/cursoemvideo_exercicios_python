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


# IRA RECEBER UM N E RETORNAR O VALOR MAIS A % INFORMADA.
def aumentar(num=1, porcento=1, convert=False):
    """
    Funcao que ira receber um numero e retornar o valor da soma da porcentagem desejada.
    :param convert: se True retorna o valor convertido para monetario.
    :param num: um numero racional
    :param porcento: recebe um numero inteiro e positivo
    :return: retorna o valor da soma da porcentagem aplicada ao valor passado.
    """
    num = num + num * (porcento/100)
    if convert:
        return converte(num)
    else:
        return num


# IRA RECEBER UM N E RETORNAR O VALOR MENOS A % INFORMADA
def diminuir(num=1, porcento=1, convert=False):
    """
Funcao que ira receber um numero e retornar o valor da soma da porcentagem que deseja subtrair.
    :param num: um numero racional
    :param porcento: recebe um numero inteiro e positivo
    :return: retorna o valor do soma da porcentagem que deseja subtrair aplicada ao valor passado.
    """
    num = num - num * (porcento / 100)
    if convert:
        return converte(num)
    else:
        return num


# IRA RECEBER UM N E RETORNAR O DOBRO DO VALOR INFORMADO
def dobro(num=1, convert=False):
    num = num * 2
    if convert:
        return converte(num)
    else:
        return num


# IRA RECEBER UM N E RETORNAR A METADE DO VALOR INFORMADO
def metade(num=1, convert=False):
    num = num / 2
    if convert:
        return converte(num)
    else:
        return num


def converte(num=1.0):
    num = f'R$ {num:.2f}'
    num = str(num)
    return num.replace('.', ',')


def resumo(num, sum_porcento=80, sub_porcento=35):
    print('~'*30)
    print('RESUMO DO VALOR'.center(30))
    print('~'*30)
    print(f'Preço analisado: \t{converte(num)}')
    print(f'Dobro do preço: \t{dobro(num, True)}')
    print(f'Metade do preço: \t{metade(num, True)}')
    print(f'{sum_porcento} de aumento: \t\t{aumentar(num, sum_porcento, True)}')
    print(f'{sub_porcento} de redução: \t\t{diminuir(num, sub_porcento, True)}')
    print('____________________________')