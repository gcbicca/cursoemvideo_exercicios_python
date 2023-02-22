"""
Modulo que ira ter funcoes que imprime na tela
"""
from menu_de_cadastro.arquivo import *
from time import sleep


def leiaint(txt):
    """
    Funcao que ira receber um valor inteiro, caso digitado errado ira mostrar uma msg.
    :param txt: Digite o texto que deseja mostrar para pedir ao usuario
    :return: retorna o valor digitado pelo usuario
    """
    while True:
        try:
            n = int(input(txt))

            # n = str(input(txt)).strip()
        except:
            print('ERRO: Porfavor digite um número inteiro válido!')
        else:
            n = int(n)
            return n
        break


def imptitulo(txt):
    print('_' * 50)
    txt = txt.upper().strip()
    print(f'  {txt.center(40)}')
    print('_' * 50)


"""def impcadastro(lista):
    imptitulo('pesssoas cadastradas')
    if not lista:
        with open('cursoemvideo.txt', 'r') as file_content:
            content = file_content.read()
            print(content)
    sleep(0.5)
    for i in lista:
        print(f'{i["nome"]:<20} {i["idade"]:>10} anos')"""


"""def cadastro():
    pessoa = {}
    imptitulo('novo cadastro')
    pessoa['nome'] = str(input('NOME: ')).strip().title()
    pessoa['idade'] = leiaint('IDADE: ')
    data.append(pessoa.copy())
    print(f'Novo registro de {pessoa["nome"]} adicionado!')"""


def menu(lista, data=[]):
    """global file_content
    with open('cursoemvideo.txt', 'x+') as file_content:
        file_content.write('inicio\n')
        print('Arquivo cursoemvideo.txt criado com sucesso!')"""
    while True:
        imptitulo('Menu principal')
        sleep(0.5)
        c = 1
        for i in lista:
            print(f'\033[33m{c}\033[m - \033[34m{i}\033[m')
            c += 1
        print('_' * 50)
        opcao = leiaint('\033[32mSua Opção:\033[m ')
        print('_' * 50)
        if opcao == 1:
            arquivo = 'cursoemvideo.txt'
            lerArquivo(arquivo)
            """impcadastro(data)"""
        if opcao == 2:
            nome = str(input('NOME: ')).strip().title()
            idade = leiaint('IDADE: ')
            arquivo = 'cursoemvideo.txt'
            cadastrar(arquivo, nome, idade)
            """cadastro(data)"""
        if opcao == 3:
            imptitulo('Saindo do sistema! Até logo')
            break




