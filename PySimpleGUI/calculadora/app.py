from operator import truediv
import PySimpleGUI as sg

WIN_W = 30
WIN_H = 50

layout_menu = [
    [
        'Files', ['Exit']
    ],
    [
        'Help', ['About']
    ]
]

layout = [
    [sg.Menu(layout_menu)],
    [
        sg.Input('0', size=(int(WIN_W/2), 1), font=('Consolas', 20), key='-BOX-'),
        sg.Button('<', font=('Consolas', 20), key='-BACKARROW-'),
        sg.Button('C', font=('Consolas', 20), key='-CLEAR-')
    ],
    [
        sg.Button('7', font=('Consolas', 20), key='-SEVEN-'),
        sg.Button('8', font=('Consolas', 20), key='-EIGHT-'),
        sg.Button('9', font=('Consolas', 20), key='-NINE-'),
        sg.Button('+', font=('Consolas', 20), key='-PLUS-'),
        sg.Button('*', font=('Consolas', 20), key='-TIMES-'),
    ],
    [
        sg.Button('4', font=('Consolas', 20), key='-FOUR-'),
        sg.Button('5', font=('Consolas', 20), key='-FIVE-'),
        sg.Button('6', font=('Consolas', 20), key='-SIX-'),
        sg.Button('-', font=('Consolas', 20), key='-MINUS-'),
        sg.Button('/', font=('Consolas', 20), key='-DIV-'),
    ],
    [
        sg.Button('1', font=('Consolas', 20), key='-ONE-'),
        sg.Button('2', font=('Consolas', 20), key='-TWO-'),
        sg.Button('3', font=('Consolas', 20), key='-THREE-'),
        sg.Button('0', font=('Consolas', 20), key='-ZERO-'),
        sg.Button('=', font=('Consolas', 20), key='-RESULT-'),
    ]
]

class appCalculator():
    def __init__(self):
        self.window = sg.Window(
            'Calculator', 
            layout=layout, 
            margins=(1, 1), 
            resizable=True, 
            return_keyboard_events=True
        )
        self.result = 0
        self.operations = ''
        self.window.read(timeout=10)
        for i in range(1, 5):
            for button in layout[i]:
                button.expand(expand_x=True, expand_y=True)
        
    def about(self):
        sg.popup('About', 'Criado por danielbernardino747')

    def resulter(self):
        if self.operations == '+':
            return float(self.result) + float(self.event['-BOX-'])
        elif self.operations == '-':
            return float(self.result) - float(self.values['-BOX-'])
        elif self.operations == '*':
            return float(self.result) * float(self.values['-BOX-'])
        elif self.operations == '/':
            return float(self.result) / float(self.values['-BOX-'])

    def start(self):
        while True:
            event, self.values = self.window.read()

            if event in (None, 'Exit', sg.WIN_CLOSED):
                break

            elif event in ('About'):
                self.about()
            
            elif event in ('-ONE-'):
                if self.values['-BOX-'] == '0':
                    self.window['-BOX-'](value='1')
                else:
                    self.window['-BOX-'](value=self.values['-BOX-'] + '1')
            
            elif event in ('-TWO-'):
                if self.values['-BOX-'] == '0':
                    self.window['-BOX-'](value='2')
                else:
                    self.window['-BOX-'](value=self.values['-BOX-'] + '2')
            
            elif event in ('-THREE-'):
                if self.values['-BOX-'] == '0':
                    self.window['-BOX-'](value='3')
                else:
                    self.window['-BOX-'](value=self.values['-BOX-'] + '3')
            
            elif event in ('-FOUR-'):
                if self.values['-BOX-'] == '0':
                    self.window['-BOX-'](value='4')
                else:
                    self.window['-BOX-'](value=self.values['-BOX-'] + '4')
            
            elif event in ('-FIVE-'):
                if self.values['-BOX-'] == '0':
                    self.window['-BOX-'](value='5')
                else:
                    self.window['-BOX-'](value=self.values['-BOX-'] + '5')
            
            elif event in ('-SIX-'):
                if self.values['-BOX-'] == '0':
                    self.window['-BOX-'](value='6')
                else:
                    self.window['-BOX-'](value=self.values['-BOX-'] + '6')
            
            elif event in ('-SEVEN-'):
                if self.values['-BOX-'] == '0':
                    self.window['-BOX-'](value='7')
                else:
                    self.window['-BOX-'](value=self.values['-BOX-'] + '7')
            
            elif event in ('-EIGHT-'):
                if self.values['-BOX-'] == '0':
                    self.window['-BOX-'](value='8')
                else:
                    self.window['-BOX-'](value=self.values['-BOX-'] + '8')
            
            elif event in ('-NINE-'):
                if self.values['-BOX-'] == '0':
                    self.window['-BOX-'](value='9')
                else:
                    self.window['-BOX-'](value=self.values['-BOX-'] + '9')
            
            elif event in ('-ZERO-'):
                if self.values['-BOX-'] == '0':
                    self.window['-BOX-'](value='0')
                else:
                    self.window['-BOX-'](value=self.values['-BOX-'] + '0')
            
            elif event in ('-CLEAR-'):
                self.result = 0
                self.window['-BOX-'](value=self.result)

            elif event in ('-BACKARROW-'):
                self.window['-BOX-'](value=self.values['-BOX-'][:-1])
            
            elif event in ('-PLUS-'):
                if self.operations != '':
                    self.result = self.resulter()
                else:
                    self.operations = '+'
                    self.result = self.window['-BOX-']
                self.window['-BOX-'](value='')
            
            elif event in ('-MINUS-'):
                if self.operations != '':
                    self.result = self.resulter()
                else:
                    self.operations = '-'
                    self.result = self.window['-BOX-']
                self.window['-BOX-'](value='')
            
            elif event in ('-TIMES-'):
                if self.operations != '':
                    self.result = self.resulter()
                else:
                    self.operations = '*'
                    self.result = self.window['-BOX-']
                self.window['-BOX-'](value='')
            
            elif event in ('-DIV-'):
                if self.operations != '':
                    self.result = self.resulter()
                else:
                    self.operations = '/'
                    self.result = self.window['-BOX-']
                self.window['-BOX-'](value='')
            
            elif event in ('-RESULT-'):
                self.result = self.resulter()
                self.window['-BOX-'](value=self.result)
                self.result = 0
                self.operations = ''

appCalculator().start()
            