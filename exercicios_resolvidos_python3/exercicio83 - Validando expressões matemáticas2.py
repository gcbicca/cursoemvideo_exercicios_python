expressao = str(input('Digite sua expressão com parênteses: '))
lista= []
for c in expressao:
    if c in '(':
        lista.append('(')
    elif c in ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Sua expressão está correta!')
else:
    print('Sua expressão está errada!')