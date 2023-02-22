"""Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da
digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade."""


def leiaint(txt):
    """
    Funcao que ira receber um valor inteiro, caso digitado errado ira mostrar uma msg.
    :param txt: Digite o texto que deseja mostrar para pedir ao usuario
    :return: retorna o valor digitado pelo usuario
    """
    while True:
        try:
            n = int(input(txt))

            # n = str(input(txt)).strip()
        except:
            print('ERRO: Porfavor digite um número inteiro válido!')
        else:
            n = int(n)
            return n
            break


def leiaFloat(txt):
    while True:
        try:
            n = float(input(txt))

            # n = str(input(txt)).strip()
        except (ValueError, TypeError):
            print('ERRO: Porfavor digite um número float válido!')
        except (KeyboardInterrupt):
            print('Usuario preferiu nao digitar!')
            return ''
        else:
            n = n
            return n
            break


print(leiaint('Digite um numero inteiro: '))
print(leiaFloat('Digite um numero float: '))
