import menu_de_cadastro.imprime_tela
from menu_de_cadastro.imprime_tela import *


def arquivoExiste(nome):
    try:
        file_object = open(nome, 'rt')
        file_object.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        file_object = open(nome, 'w+')
        file_object.close()
    except:
        print('Erro na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    try:
        abrir = open(nome, 'r')
    except:
        print('Houve um errro ao ler o arquivo')
    else:
        menu_de_cadastro.imprime_tela.imptitulo('CADASTRO ARQUIVO')
        for linha in abrir:
            """
gabriel;18
['gabriel;18', 'joao;10']
['gabriel', '18']"""
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>5} anos')


def cadastrar(nome_arquivo, nome='desconhecido', idade=0):
    try:
        abrir = open(nome_arquivo, 'a')
        abrir.write(f'{nome};{str(idade)}\n')
    except:
        print('Erro no cadastro!')