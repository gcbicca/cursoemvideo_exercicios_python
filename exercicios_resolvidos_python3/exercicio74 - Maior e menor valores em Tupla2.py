from random import randint
n = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))#Coloque ( ) entre o código e ele estará em uma tupla
#Pode-se replicar quantas vezes eu quiser a função dentro da tupla.
for c in n:
    print(c, end= ' ')#end= ' ' Faz os caracteres serem empressos separados por...
print(f'\nO maior número é {max(n)}')#\n faz com que a linha seja impressa em baixo
print(f'O menor número é {min(n)}')