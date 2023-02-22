"""
Faça um programa que tenha uma FUNÇÃO NOTAS() que pode receber várias notas de alunos e vai retornar um DICIONÁRIO com
as seguintes informações:
    - Quantidade de notas
    - A maior nota
    - A menor nota
    - A média da turma
    - A situação (opcional)

Adicione também as DOCSTRING da função.

Ex:
# Programa Principal
resp = notas(5.5, 9.5, 10 , 6.5, sit=True)
print(resp)
linha
dicionário(){'total':4, 'maior':10, 'menor':5.5, 'media':7.87, 'situação': BOA}
help(notas)
notas(*n, sit=False)
    -> Função para analisar notas e situações de vários alunos.
        :param n: uma ou mais notas dos alunos (aceita várias)
        :param sit: valor opcional, indicando se deve ou não adicionar a situação
        :return: dicionário com várias informações sobre a situação da turma.
"""


# função notas que receberá várias notas e armazenará os dados em um dicionário retornando-o no final
def notas(*nota, situacao=False):
    """
    :param nota: uma ou mais notas dos alunos (aceita várias)
    :param situacao: valor opcional, indicando se deve ou não adicionar a situação
    :return: retorna um dicionário com os valores
    """
    dataset = {}
    dataset['numero_de_notas'] = len(nota)
    dataset['nota_maxima'] = max(nota)
    dataset['nota_minima'] = min(nota)
    dataset['media da turma'] = sum(nota) / dataset['numero_de_notas']
    if situacao:
        if dataset['media da turma'] >= 7:
            dataset['situacao'] = 'Excelente'
        elif 6 <= dataset['media da turma'] < 7:
            dataset['situacao'] = 'Regular'
        else:
            dataset['situacao'] = 'Péssima'
    return dataset


resp = notas(5.5, 9.5, 10, 6.5)
print(resp)
help(notas)
