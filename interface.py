#Interface gráfica

from function import *

import PySimpleGUI as psg

layou_frame = [
    [psg.Radio('Conversão Farenheit', 'btnRadio1', key='Farenheit', default= True)],
    [psg.Radio('Conversão Celsius', 'btnRadio1', key='Celsius')]
]

layout = [
    [psg.Text('Informe um número: '), psg.InputText(key='numero'), psg.Frame('Opções: ', layou_frame)],
    [psg.Text("", key='resultado')],
    [psg.Button('Calcular'), psg.Button('Limpar')]
]

window = psg.Window('Conversor de temperatura', layout)

while True:
    number, valor = window.read()

    if number == psg.WIN_CLOSED:
        break
    else:
       if valor['Farenheit']:
           num = C_para_F(int(valor['numero']))
           window['resultado'].update(f'{valor["numero"]}! = {num}')
       else:
           window['resultado'].update(F_para_C(int(valor['numero'])))

window.close()
