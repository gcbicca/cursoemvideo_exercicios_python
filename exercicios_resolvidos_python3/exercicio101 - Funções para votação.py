"""Crie um programa que tenha uma FUNÇÃO chamada VOTO() que vai receber como PARÂMETRO o ANO DE NASCIMENTO de uma pessoa
RETORNANDO um valor LITERAL indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.
ex:
linha -
input, em que ano você nasceu?
com 18 anos o voto é obrigatório.
com 65+ o voto é opcional
a frase é um retorno da função
"""
# Importa o ano atual
from datetime import date


# Essa função vai receber um parâmetro que será ano de nascimento e retornará se ela pode votar
def voto(ano_nascimento):
    """
    Função irá exibir se pode votar com base no ano de nascimento.
    :param ano_nascimento: Insira o seu ano de nascimento.
    :return: sem retorno
    """
    idade = date.today().year - ano_nascimento
    if idade < 16:
        return f'Com {idade} anos o voto é NEGADO!'
    elif 16 <= idade < 18 or idade >= 70:
        return f'Com {idade} anos o voto é OPCIONAL'
    else:
        return f'Com {idade} anos o voto é OBRIGATÓRIO!'


print('~' * 50)
nascimento = int(input('Digite o seu ano de nascimento: '))
print(voto(nascimento))