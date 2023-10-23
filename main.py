from function import C_para_F
from function import F_para_C

while True:

        print('Conversor de temperatura')

        print('1. Converter de Celsius para Fahrenheit')
        print('2. Converter de Fahrenheit para Celsius')
        print('3. Sair \n')

        Op = int(input('Opção: '))
        if Op == 1:
            C = float(input('Graus Celsius: '))
            print = ('Temperatura em Farenheit: ', C_para_F(C))
        elif Op == 2:
            F = float(input('Graus Farenheit: '))
            print = ('Temperatua em Celsius ', F_para_C(F))
        elif Op == 3:
            break
        else:
            print('Opção invalida')


