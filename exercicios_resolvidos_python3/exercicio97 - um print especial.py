"""Faça um programa que tenha uma FUNÇÃO chamada ESCREVA(), que recebe um texto qualquer como PARÂMETRO e mostre
uma mensagem com tamanho adaptável.
Ex:
ESCREVA('Olá, Mundo!')

Saída:
~~~~~~~~~~
 Olá, Mundo!
~~~~~~~~~~
"""
# Essa função irá printar de forma elegante e receberá como parâmetro um texto.


def escreva(txt):
    """Irá printar de forma elegante e receberá como parâmetro um texto."""
    tam = len(txt) + 4
    print('~'* tam)
    print(f'  {txt}')
    print('~' * tam)


# Irá pedir para o usuário inserir uma texto
texto = input('Digite um texto de sua escolha: ').strip().title()
escreva(texto)


