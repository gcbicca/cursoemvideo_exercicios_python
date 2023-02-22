'''
Crie um programa que leia o nome de uma pessoa e diga se
ela tem 'SILVA' no nome.
'''
nome = str(input('Qual é o seu nome completo? ')).strip() #Colocar o input como string e ao final colocar o strip para remover os espaços
#print('Seu nome tem Silva? {}'.format('SILVA' in nome.upper()))
nome_upper = nome.upper()
nome_teste = 'SILVA' in nome_upper #OPERADOR IN e NÃO UM MÉTODO
print('O seu nome é {}, Você possui o sobrenome Silva? {}'.format(nome, nome_teste))