""" Refaça o DESAFIO 009, mostrando a TABUADA de um número que o usuário
escolher, só que agora utilizando um LAÇO FOR."""
y = int(input('Digite o número que deseja ver a tabuada: '))
print(f'O número escolhido foi {y}')
for x in range(1,11):
    print(f'{x:2} X {y} = {x * y}') #:2 cria espaços no inicio e nesse programa alinha os resultados