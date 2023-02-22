'''
Faça um programa que leia o nome completo de uma pessoa,
mostrando em seguinda o primeiro e o último nome separadamente.
ex:Ana Maria de Souza
primeiro=Ana
último=Souza
'''
nome = str(input('Digite o nome completo: ')).strip()
nome_quebra = nome.split()
primeiro_nome = nome_quebra[0]
nome_quebra.reverse()
ultimo_nome = nome_quebra[0]
print('O nome completo digitado é {}, o seu primeiro nome é {}, sendo o último {}'.format(nome, primeiro_nome, ultimo_nome))

'''
n = str(input('Digite o seu nome completo: ')).strip()
nome = n.split()
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome(nome[len(nome)-1]))
print('Seu último nome é {}'.format(nome[-1]))
'''