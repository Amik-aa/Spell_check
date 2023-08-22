import PySimpleGUI as sg
from textblob import TextBlob, Word

sg.theme('DarkAmber')   
sg.set_options(font='Verdana 15')
layout = [  [sg.Text('SpellChecker')],
            [sg.Text('Enter a word'), sg.InputText(key='-IN-')],
            [sg.Button('Ok'), sg.Button('Cancel')]
            [sg.Multiline(disabled=True, key='-OUT-',size=(55,10))] 
         ]


window = sg.Window('SpellChecker', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    if event == 'Ok':
        w = values['-IN-']
        b = Word(w)
        window['-OUT-'].update(b.spellcheck())

window.close()
