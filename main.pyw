# hello_psg.py

import PySimpleGUI as sg
from xpinyin import Pinyin

layout = [
    [sg.Text("Hanzi to Pinyin", font="Any 20")],
    [sg.Text("Result Shown Here...", key="lblText", font="Any 15")],
    [sg.In(size=(25, 1), font="Any 20", enable_events=True, key="txtHanzi")],
    [sg.Button("OK", key="btnShow")]
]

# Create the window
window = sg.Window("H2P - By Benyamin", layout)

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "OK" or event == sg.WIN_CLOSED:
        break
    elif event == "btnShow":
        p = Pinyin()
        pinYin = p.get_pinyin(values["txtHanzi"], tone_marks='marks')
        window["lblText"].update(pinYin)


window.close()


