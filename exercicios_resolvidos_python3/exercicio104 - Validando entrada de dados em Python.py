"""
Crie um programa que tenha a FUNÇÃO LEIAINT(), que vai funcionar de forma semelhante à função INPUT() de python, só que
fazendo a VALIDAÇÃO para aceitar apenas um valor numérico.
Ex:
n = leiaInt('Digite um n')
ex:
#programa principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
linha
input, digite um número: 4
você acabou de digitar o número 4
input, digite um número: w
Vermelho() ERRO! Digite um número inteiro válido.
input, digite um número: "Espaços"
Vermelho() ERRO! Digite um número inteiro válido.
"""


# Essa função aceitará apenas um valor e verificará se é um valor numérico.
def leiaint(numero=''):
    """
    -> Essa função irá verificar se o valor inserido é numérico
    :param numero: insira um número
    :return: Retorna o valor inserido
    """
    while True:
        n_inserido = str(input(numero))
        if n_inserido.isnumeric():
            valor = int(n)
            break
        else:
            print(f'\033[1;36mERRO! Digite um número inteiro válido\033[m')
    return valor


# Programa principal
n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
