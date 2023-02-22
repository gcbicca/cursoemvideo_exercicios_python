list = []
temp = []
bigger = lower = 0
pbigger = []
plower = []
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(list) == 0:
        bigger = lower = temp[1]
    if temp[1] > bigger:
        bigger = temp[1]
    elif temp[1] < lower:
        lower = temp[1]
    list.append(temp[:])
    temp.clear()
    flag = str(input('Quer continuar [S/N]: ')).strip()[0]
    if flag in 'Nn':
        break
for p in list:
    if p[1] == bigger:
        pbigger.append(p[0])
    elif p[1] == lower:
        plower.append(p[0])
print(list)
print(f'Você cadrastrou ao todo {len(list)} pessoas.')
print(f'O maior valor cadastrado foi: {bigger}. Sendo atribuido a {pbigger}')
print(f'O menor valor cadastrado foi : {lower}. Sendo atribuido a {plower}')