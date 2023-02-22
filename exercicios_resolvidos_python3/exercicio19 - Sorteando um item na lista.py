#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
import random
aluno1 = input('Qual o nome do primeiro aluno? ')
aluno2 = input('Qual o nome do segundo aluno? ')
aluno3 = input('Qual o nome do terceiro aluno? ')
aluno4 = input('Qual o nome do quarto aluno? ')
lista = [aluno1, aluno2, aluno3, aluno4]
sorteio=random.choice(lista)
print('O aluno sorteado foi: {}'.format(sorteio))