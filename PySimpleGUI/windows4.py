import PySimpleGUI as sg

sg.theme('Dark Blue 13')

layout = [
    [sg.Text('Your typed chars appear here: '), sg.Text(size=(12,1), key='-OUTPUT-')],
    [sg.Input(key='-IN-')],
    [sg.Button('Show'), sg.Button('Exit')],
]

window =  sg.Window('Janela', layout, enable_close_attempted_event=True)

while True:
    event, values = window.read()
    print(event, values)
    if (event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT or event == 'Exit') and sg.popup_yes_no('Do you really want to exit?') == 'Yes':
        break
    if event == 'Show':
        window['-OUTPUT-'].update(values['-IN-'])