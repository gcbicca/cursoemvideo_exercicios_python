"""
Adicione ao módulo MOEDA.PY criado nos desafios anteriores, uma função chamada RESUMO(), que mostre na tela algumas
informções geradas pelas funções que já temos no módulo criado até aqui.
"""
from utilidadesCeV import moeda
from utilidadesCeV import dado


# PROGRAMA PRINCIPAL
preco = dado.leiadado('Digite um preço: R$')
moeda.resumo(preco, 40, 25)