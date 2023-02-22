'''
Crie um programa que leia o nome de uma cidade e diga se ela
começa ou não com o nome 'SANTO'
'''
nome_cidade = str(input('Digite o nome de um cidade: ')).strip() #Colocar o input como string e ao final colocar o strip para eliminar os espaços no inicio e final
#print(nome_cidade[:5].upper == 'SANTO')
nome_cidade_upper = nome_cidade.upper()
nome_cidade_quebra = nome_cidade_upper.split()
nome_cidade_resultado00 = nome_cidade_quebra[0]
teste = 'SANTO' in nome_cidade_resultado00
print('O nome da cidade digito foi {}, e ela possui Santo em seu nome? {}'.format(nome_cidade, teste))