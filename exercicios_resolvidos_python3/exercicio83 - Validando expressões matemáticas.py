"""
Crie um programa onde o usuário digite uma EXPRESSÃO qualquer que use PARÊNTESES. Seu aplicativo deverá
analisar se a expressão passada está com os parênteses abertos e fechados na ORDEM CORRETA.
"""
lista = []
lista_pos = []
expressao = input('Digite uma expressão que use parênteses: ')
print(f'A expressão é {expressao}')
for c in expressao:
    if c == '(' or c == ')':
        lista.append(c)
for pos, valores in enumerate(lista):
    lista_pos.append(pos)
    lista_pos.append(valores)
for c in range(len(lista_pos)):
    if len(lista) % 2 == 1:
        print('A expressão está errada! Está faltando parenteses complementares!')
        break
    if lista_pos[c] == ')' and c <= 2:
        print('A expressão está errada! Iniciou com um parenteses para o lado errado!')
        break
    elif lista_pos[c] == '(':
        if lista_pos[c+2] == ')':
            if len(lista_pos) == c+3:
                print('A expressão está correta')
                break
        elif lista_pos[c+2] == '(':
            print(f'A expressão está errada com um parenteses para o lado errado!')
            break
    elif lista_pos[c] == ')':
        if lista_pos[c-2] == '(':
            if len(lista_pos) == c+1:
                print('A expressão está correta')
        elif lista_pos[c-2] == ')':
            print('A expressão está errada! Com um parenteses para o lado errado!')
            break
