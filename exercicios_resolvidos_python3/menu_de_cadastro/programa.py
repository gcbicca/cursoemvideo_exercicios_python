from menu_de_cadastro.imprime_tela import *
from menu_de_cadastro.arquivo import *

arquivo = 'cursoemvideo.txt'
if not arquivoExiste(arquivo):
    criarArquivo(arquivo)

menu(['Ver pessoas cadastradas', 'Cadastrar novas pessoas', 'Sair do sistema'])