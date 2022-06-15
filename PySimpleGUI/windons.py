import PySimpleGUI as sg

sg.theme('Dark Blue 13') 

layout = [
    [sg.Text('Digite um número abaixo')],
    [sg.Input(password_char='*')],
    [sg.OK(), sg.Cancel()]
]

window = sg.Window('Digite um número', layout)

event, values = window.read()

window.close()

sg.popup(values[0])