"""
Crie uma TUPLA preenchida com os 20 PRIMEIROS colocados da Tabela do CAMPEONATO BRASILEIRO DE FUTEBOL, na ordem de colocação
Depois mostre:
A) Apenas os 5 PRIMEIROS colocados.
B) Os ÚLTIMOS 4 colocados da tebela.
C) Uma lista com os times em ORDEM ALFABÉTICA.
D) Em que POSIÇÃO na tebela está o time da CHAPECOENSE.
EX: Saída tudo em tuplas.
"""
tabela = ('Flamengo','Santos', 'Palmeiras', 'Grêmio', 'Athletico Paranaense', 'São paulo',
          'Internacional', 'Corinthians', 'Fortaleza', 'Goiás', 'Bahia', 'Vasco da Gama',
          'Atlético', 'Fluminense', 'Botafogo', 'Ceará', 'Cruzeiro', 'Csa', 'Chapecoense', 'Avaí')
chape = tabela.index('Chapecoense')
print(f'Os 5 primeiros colocados são: {tabela[0:5]}')
print(f'Os últimos 4 colocados da tabela são: {tabela[16:20]}')#Ou -4: que significa do menos 4 até o último.
print(f'Os nomes dos times em ordem alfabética são: {sorted(tabela)}')#Sorted retorna uma lista em ordem crescente.
#Posso utilizar no print mesmo {tabela.index("Chapecoense")+1}
print(f'O time da Chapecoense está na posição {chape+1}')

