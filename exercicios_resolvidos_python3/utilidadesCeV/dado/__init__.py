"""
Dentro do pacote UTILIDADESCeV que criamos no DESAFIO 111, temos um MÓDULO chamado DADO. Crie uma função chamda
LEIADINHEIRO() que seja capaz de funcionar como a função INPUT(), mas com uma VALIDAÇÃO DE DADOS para aceitar apenas
valores que sejam MONETÁRIOS.
"""
def leiadado(txt):
    while True:
        valor = str(input(txt)).strip()
        if valor == '':
            print(f'ERRO ({valor}) é um preço inválido!')
        elif valor.isalpha():
            print(f'ERRO ({valor}) é um preço inválido!')
        elif valor.isnumeric():
            valor = float(valor)
            break
        elif '.' in valor:
            valor = float(valor)
            break
        elif ',' in valor:
            valor = valor.replace(',', '.')
            valor = float(valor)
            break
        if valor.isnumeric():
            valor = float(valor)
            break
    return valor

