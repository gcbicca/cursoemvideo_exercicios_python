"""
Crie um programa que tenha uma TUPLA com várias palavras (Não usar acentos).
Depois disso você deve mostrar, para cada palavra, quais as suas VOGAIS.
"""
palavras = ('amor', 'paixao', 'vida', 'cosmos', 'estrelas')
print(palavras)
pa = ''
for p in palavras:
    print(f'\nA palavra {p.upper()} tem as vogais: ', end='')#p.upper() deixa em maiusculas a variavel p
    words = p
    for vogais in words:
        if vogais.lower() in 'aeiou':
            print(f'{vogais}', end=' ')

