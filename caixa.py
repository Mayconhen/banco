from conta import contas
import pandas
from PySimpleGUI import PySimpleGUI as sg

<<<<<<< HEAD
#layou
sg.theme('Reddit')
layout = [
    [sg.Text('Conta:'), sg.Input(key='Conta')],
    [sg.Button('Mostrar')]
]
=======

conta = int(input())
contas.extrato(conta)





>>>>>>> 469fbce9c4184a867cf7e839586f6e685ab14510

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
            
