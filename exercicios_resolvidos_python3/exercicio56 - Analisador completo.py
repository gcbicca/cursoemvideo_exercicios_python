""" Desenvolva um programa que leia o NOME, IDADE e SEXO  de 4 PESSOAS. No final do programa mostre:
A média de idade do grupo
Qual é o nome do homem MAIS VELHO.
Quantas mulheres têm MENOS DE 20 anos."""
lst_nome = []
lst_idade = []
lst_sexo = []
nomevelho = ''
maioridadehomem = 0
contador_w20 = 0
for c in range(1,5):
    print(f'============= {c}ª PESSOA ===============')
    nome = input(f'Digite o nome da {c}ª pessoa: ').upper().strip()
    idade = int(input(f'Digite a idade da {c}ª pessoa: '))
    sexo = int(input(f'Escolha a opção relacionada ao sexo [1] para Homem e [2] para Mulher: '))
    if sexo == 1 and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo == 2 and idade < 20:
        contador_w20 += 1
    lst_nome += [nome]
    lst_idade += [idade]
    lst_sexo += [sexo]
soma_idade = 0
for soma in lst_idade:
    soma_idade += soma
media = soma_idade / c
print(f'A média de idade do grupo em questão é {media}.\n'
      f'O nome dos Homem mais velho é: {nomevelho}.\n'
      f'A quantidade de mulher(s) menor(es) de 20 anos é {contador_w20}.')
'''idade_max = max(lst_idade) #Analisa o número máx dentro da lista
posi_idade = lst_idade.index(idade_max)#Acha a posição na lista do termo em questão
nome_idade_max = lst_nome[posi_idade]'''

