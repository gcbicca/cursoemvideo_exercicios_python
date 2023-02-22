""" Faça um programa que leia o ano de nascimento de um jovem
e informe, de acordo com sua idade:
Se ele AINDA VAI SE ALISTAR ao serviço militar. A idade para se alistar é no ano que completar 18 de 1° janeiro até 30 abril.
Se é a HORA DE SE ALISTAR.
Se já PASSOU DO TEMPO  do alistamento.
Seu programa também deverá mostrar o tempo que faltou ou que passou do prazo.
"""
from datetime import date #Importa a biblioteca que pega a data atual
ano_atual = date.today().year #Comando para pegar a data
print('\033[1;36mBem-vindo(a) ao programa de verificação para o alistamento militar!\033[m')
sexo = int(input('Digite o número referente a opção do seu sexo, sendo, [1] MASCULINO e [2] FEMININO: '))
if sexo == 2:
    print('Bem-vinda ao alistamento militar!\nNo Brasil o alistamento militar não é obrigatório para mulheres, sabendo disso, escolha uma opção abaixo!')
    opcao = int(input('Digite [1] se deseja se alistar ao serviço militar e [2] caso não deseje: '))
    if opcao == 1:
        print('Braço Forte - Mão Amiga, vamos verificar se você tem idade suficiente para se alistar!')
        ano_nasc = int(input('Digite o seu ano de nascimento com 4 dígitos: '))
        idade = ano_atual - ano_nasc
        if idade < 18:
            print(f'Ainda faltam {18 - idade} ano(s) para o seu ano de alistamento, portanto, fique ligada! ')
        elif idade == 18:
            print(f'Você está em idade de se alistar, uma junta militar mais próxima e se aliste.')
        elif idade > 18:
            print(f'Se você ainda não se alistou, está em tempo de se alistar, portanto, vá o mais rápido possível a junta militar mais próxima!')
    elif opcao == 2:
        print('Você está dispensada de qualquer outra formalidade perante o serviço militar! Obrigado pela atenção.')
    else:
        print('Opção inválida! Digite uma opção correspondente.')
elif sexo == 1:
    ano_nasc = int(input('Digite o seu ano de nascimento com 4 dígitos: '))
    idade = ano_atual - ano_nasc
    if idade < 18:
        print(f'Ainda faltam {18 - idade} ano(s) para o seu ano de alistamento, portanto, fique ligado! ')
        print(f'O ano do seu alistamento será em {(18 - idade) + ano_atual}.')
    elif idade == 18:
        print(f'Você está em idade de se alistar, se ainda não se alistou, busque a junta militar mais próxima.')
    elif idade > 18:
        print(f'Se você ainda não se alistou, está atrasado em {idade - 18} ano(s), portanto, vá o mais rápido possível a junta militar mais próxima!')
        print(f'O ano em que você deveria ter se alistado era {idade - 18- ano_atual}.')
else:
    print('Opção inválida! Digite uma opção correspondente.')