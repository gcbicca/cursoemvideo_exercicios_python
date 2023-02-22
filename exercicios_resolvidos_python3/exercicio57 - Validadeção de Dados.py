'''
Faça um programa que leia o SEXO de uma pessoa, mas só aceite
os valores 'M' ou 'F'. Caso esteja errado, peça a digitação
novamente até ter um valor correto.
'''
sexo = str(input('Digite o seu sexo [M/F]: ')).upper().strip()#[0]Pega apenas a primeira letra
while sexo not in 'MmFf': #Dentro da string Sexo não tem M ou m ou F ou f entra no laço, SE FALSO sai do laço ou nem entra
    sexo = str(input('Dados inválidos. Porfavor digite um valor correspodente para o sexo [M/F]: ')).upper().strip()
print(f'A opção selecionada corresponde ao sexo {sexo}.')
print('Fim')
'''
Você pode criar uma lista com as palavras que você quer que o programa aceite.
Por exemplo:
while sexo not in ['M', 'F', 'HOMEM', 'MULHER', 'MASCULINO', 'FEMININO']:
    sexo = input('Informe seu sexo: ').split().upper()
'''

