import PySimpleGUI as sg
num = 0

layout = [
    [sg.Text(num)],
    [sg.Button("hi")]
]

window = sg.Window("the box", layout)

while True:
    event, values = window.read()
    if event == "hi":
        num = num+1
        layout = [
    [sg.Text(num)],
    [sg.Button("hi")]
    ]
    window = sg.Window("the box", layout)