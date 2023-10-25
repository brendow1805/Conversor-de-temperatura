from function import *

while True:

    print('\n Conversor de temperatura')

    print('1. Converter de Celsius para Fahrenheit')
    print('2. Converter de Fahrenheit para Celsius')
    print('3. Sair \n')

    Op = int(input('Opção: ').strip())

    if Op == 1:
        C = float(input('Graus Celsius: '))
        F = C_para_F(C)
        print(f'{C}°C é igual a {F}°F')
    elif Op == 2:
        F = float(input('Graus Farenheit: '))
        C = F_para_C(F)
        print(f'{F}°F é igual a {C}°C')
    elif Op == 3:
        print('Tchau!')
        break
    else:
        print('Opção invalida')


