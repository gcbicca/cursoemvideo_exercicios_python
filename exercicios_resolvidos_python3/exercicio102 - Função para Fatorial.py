"""
Crie um programa que tenha uma FUNÇÃO FATORIAL() que receba dois parâmetros:
O primeiro que indique o NÚMERO a calcular
O segundo chamdo SHOW, que será um valor LÓGICO(OPCIONAL) indicando se será mostrado ou não na tela o processo de
cálculo do fatorial.
ex:
#programa principal
print(f(5, show=True)
linha
5 x 4 x 3 x 2 x 1 = 120
print(f(5, show=False)
120
help(f)
-> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
"""


# Essa função irá mostrar o cálculo fatorial de números inteiros e receberá dois parâmetros.
def fatorial(numero, show=False):
    """
    Essa função irá calcular o fatorial de um número inteiro, e poderá mostrar o desenvolvimento do cálculo.
    :param numero: Insira um número inteiro.
    :param show: (opcional) Insira True se quer mostrar o desenvolvimento e False caso não.
    :return: O valor Fatorial de um número.
    """
    f = 1
    for c in range(numero, 0, -1):
        if show:
            print(f'{c}', 'x ' if c > 1 else '= ',  end='')
        f *= c
    return f


print('~' * 50)
print(fatorial(5, show=False))
