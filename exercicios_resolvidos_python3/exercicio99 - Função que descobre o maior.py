"""Faça um programa que tenha uma FUNÇÃO chamada MAIOR(), que receba vários PARÂMETROS com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual dele é o MAIOR."""


# Essa função irá definir o maior valor que será passado para ela.
def maior(*lista):
    """Essa função irá exibir o maior valor passado como argumento."""
    maximo = max(lista)
    print(f'O valor máximo que foi passado como parâmetro/argumento é {maximo}')


maior(1, 20, 3, 4, 5, 6)
