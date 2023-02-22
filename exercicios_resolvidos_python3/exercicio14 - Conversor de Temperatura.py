#
#Output foi informe a temperatura em °C:
#A temperatura de 31.5 °C corresponde a 88.7 °F
#(0 °C × 9/5) + 32 = 32 °F fórmula de convesão
temp_celsius = float(input('Informe a temperatura em Celsius: '))
temp_fahrenheit = (temp_celsius * 9/5) + 32
print('A temperatura em Celsius é {}°C \nA temperatura em Fahrenheit é: {}°F'.format(temp_celsius, temp_fahrenheit))
