"""
Crie um programa que leia o nome completo de uma pessoa e
mostre:
#O nome com todas as letras maiúsculas
#O nome com todas minúsculas
#Quantas letras ao todo(sem considerar espaços)
#Quantas letras tem o primeiro nome.
"""
nome = str(input('Qual é o seu nome completo? '))
#nome = str(input('Qual é o seu nome completo? ')).strip() - Esse strip no final tira os espaços no inicio e no final
nome_upper = nome.upper()
#print('Seu nome em maiúsculo é {}'.format(nome.upper()))
nome_lower = nome.lower()
#print('Seu nome em minúsculas é {}'.format(nome.lower()))
n_letras_trat = nome.split() #Necessita-se quebrar o nome em listas com cada palavra
#split retorna: ['Gabriel', 'Chaves', 'Bicca']
n_letras_trat01 = ''.join(n_letras_trat) #Depois se junta cada lista contendo as palavras uma ao lado da outra
n_letras = len(n_letras_trat01) #contasse quantas letras tem com todas as palavras juntas sem contar os espaços
#print('Seu nome tem ao {} letras'.format(len(nome))) - Conta com os espaços
#print('Seu nome tem ao {} letras'.format(len(nome) - nome.count(' '))) #Conta quantas letras tem junto com os espaços mas, ao final subtrai os espaços
n_letras_firstname = nome.split() #Quebrei dnv
#print('Seu primeiro nome tem {} letras'.format(nome.find(' '))) - Irá achar a posição do primeiro espaço, sendo análogo a quantidade de caracteres do primeiro nome
n_letras_firstname_01 = n_letras_firstname[0] #Criei uma variável para a primeira palavra quebrada dentro da lista
n_letras_firstname_result = len(n_letras_firstname_01)#Contei a primeira palavra quebrada dentro da lista
#print('Seu primeiro nome é {} e ele tem {} letras'.format(n_letras_firstname[0], len(n_letras_firstname[0])))
print('O seu nome completo é {}'.format(nome))
print('O seu nome com todas as letras maísculas é {}'.format(nome_upper))
print('O seu nome com todas as letras minúsculas é {}'.format(nome_lower))
print('O seu nome completo tem {} letras sem contar os espaços'.format(n_letras))
print('O seu primeiro nome tem {} letras'.format(n_letras_firstname_result))
