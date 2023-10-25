#Interface gráfica


import PySimpleGUI as psg

layout_frame = [
    [psg.Radio('Conversão Farenheit', 'btnRadio1', key='Farenheit')],
    [psg.Radio('Conversão Celsius', 'btnRadio 1', key='Celsius',default=True)
]]

layout = [
    [psg.Text('Informe um número: '), psg.In(Key='numero'), psg.Frame('Opções: ', layout_frame) ],
    [psg.Text("", key='resultado')],
    [psg.Button('Calcular'), psg.Button('Limpar')],
]

window = psg.Window('Conversor de temperatura', layout)

    while True: