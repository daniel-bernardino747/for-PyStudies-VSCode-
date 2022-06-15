import PySimpleGUI as sg

for i in range(5000):
    sg.one_line_progress_meter(
        'Título', 
        i+1, 
        5000,
        orientation='h',
        size=(25,5),
        )