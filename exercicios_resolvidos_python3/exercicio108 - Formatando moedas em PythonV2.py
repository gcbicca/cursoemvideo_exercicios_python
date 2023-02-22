"""
Adapte o código do DESAFIO 107, criando uma função adicional chamada MOEDA() que consiga mostrar os valores como um
valor monetário formatado.
ex: R$420,00
"""
import moeda
# PROGRAMA PRINCIPAL

valor = float(input(f'Digite um valor que deseja ver formatado como monetário: '))
print(f'O valor formatado: {moeda.convert(valor)}')