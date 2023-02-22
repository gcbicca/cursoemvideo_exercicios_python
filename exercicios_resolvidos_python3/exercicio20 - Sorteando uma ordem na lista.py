
from random import shuffle
#Função que significa embaralhar, só funciona em listas, ela irá embaralhar a sequencia.
#O mesmo professor do desafio anterior que sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
aluno1 = input('Qual o nome do primeiro aluno? ')
aluno2 = input('Qual o nome do segundo aluno? ')
aluno3 = input('Qual o nome do terceiro aluno? ')
aluno4 = input('Qual o nome do quarto aluno? ')
lista = [aluno1, aluno2, aluno3, aluno4]
sorteio = shuffle(lista)
print('A sequencia selecionada é: {}'.format(sorteio))
