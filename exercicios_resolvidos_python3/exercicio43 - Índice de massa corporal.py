""" Desenvolva uma lógica que leia o peso e a altura, calcule seu
IMC e mostre seu status, de acordo com a tabela abaixo:
Abaixo de 18.5: Abaixo do Peso
Entre 18.5 e 25: Peso ideal
25 até 30: Sobrepeso
30 até 40: Obesidade
Acima de 40: Obesidade mórbida
"""
print('\033[1;36m-=-\033[m'*50)
print('\033[1;33mCalculadora de IMC(Índice de massa corporal)\033[m')
print('\033[1;36m-=-\033[m'*50)
peso = float(input('Digite o seu peso (kg), caso coloque as gramas utilize o ponto para separar (kg) de (g): '))
altura = float(input('Digite a sua altura (m), para separar o metro dos centímetro utilize o ponto: '))
IMC = peso / (altura**2)
if IMC < 18.5:
    print(f'O seu IMC é {IMC:.2f} e você está ABAIXO DO PESO')
elif IMC >= 18.5 and IMC <= 25:
    print(f'O seu IMC é {IMC:.2f} e você está com o PESO IDEAL')
elif IMC > 25 and IMC <= 30:
    print(f'O seu IMC é {IMC:.2f} e você está com SOBREPESO, procure se cuidar para não prejudicar sua saúde!')
elif IMC > 30 and IMC <= 40:
    print(f'O seu IMC é {IMC:.2f} e você está com OBESIDADE, procure um médico para lhe auxíliar no proagnóstico, pois, é uma condição que pode lhe levar a diversas outras doenças!')
else:
    print(f'O seu IMC é {IMC} e você está com OBESIDADE MÓRBIDA, procure um médico o mais rápido possível para lhe auxíliar no proagnóstico,\n'
          f'a obesidade mórbida aumenta o risco de desenvolver doenças crônicas degenerativas, portanto, é uma condição com elevado risco a saúde. ')