from conta import contas
import pandas
from PySimpleGUI import PySimpleGUI as sg

#layou
sg.theme('Reddit')
layout = [
    [sg.Text('Conta:'), sg.Input(key='Conta')],
    [sg.Button('Mostrar')]
]

#janela
janela = sg.Window("Banquinho xereca", layout)

#ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Mostrar':
        if valores['Conta'] == '0':
            sg.Print(sg.Window("Saldo:{}".format(contas.extrato())))
            
