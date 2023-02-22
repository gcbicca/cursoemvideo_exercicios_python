"""
Crie um programa que leia NOME e DUAS NOTAS de vários alunos e guarde tudo em uma LISTA COMPOSTA.
No final, mostre um BOLETIM contendo a MÉDIA de cada um e permita que o usuário possa mostrar as
NOTAS  de cada aluno individualmente.
"""
temp = []
lista = []
while True:
    temp.append(str(input('Nome: ')).title())
    temp.append(float(input('Nota 1: ')))
    temp.append(float(input('Nota 2: ')))
    lista.append(temp[:])
    temp.clear()
    flag = str(input('Você deseja cadastrar mais [S/N]?: ')).strip()[0]
    if flag in 'Nn':
        break
print('=-' * 30)
print('         BOLETIM DAS MÉDIAS DE CADA ALUNO      ')
print('=-' * 30)
print(f'{"No.":<4}{"Nome":<10}{"Média":>8}')
for i, l in enumerate(lista):
    print(f'{i:<4}{lista[i][0]:<10}{(lista[i][1] + lista[i][2])/2:>8}')
    print('-' * 60)
flag2 = str(input('Você deseja ver uma nota individualmente [S/N]: ')).strip()[0]
while True:
    if flag2 in 'Ss':
        nome_aluno = str(input('Qual o nome do aluno que deseja verificar a nota? (No interrompe) ')).title()
        for i, l in enumerate(lista):
            if nome_aluno in lista[i]:
                print(f'O aluno(a) {nome_aluno} possui a nota média {(lista[i][1] + lista[i][2])/2}.\n'
                      f'Nota avaliação 1: {lista[i][1]}\n'
                      f'Nota avaliação 2: {lista[i][2]}')
                print('-=' * 30)
                break
    if nome_aluno == 'No':
        break