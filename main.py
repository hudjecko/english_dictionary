import pandas as pd
import PySimpleGUI as sg

df = pd.read_csv("dictionary.csv")
sg.theme("Dark Blue 12")
text1 = sg.Text("Enter a word:")
input = sg.InputText(tooltip="Enter Word...",size=(35, 10),key="input")
output = sg.Text(size=(40,10),key="output",font=("Helvetica", 10))
button = sg.Button("Define",key="def",bind_return_key=True)
output_input = sg.Text(key="output_reci",size=(10,10))
window = sg.Window("DICTIONARY",
                    layout=[[text1, input,button], [output_input, output]])


while True:
    event, values = window.read()
    match event:
        case sg.WIN_CLOSED:
            break
        case "def":
            if values["input"] in df['word'].unique():
                definition = df.loc[df["word"] == values["input"]]["definition"].squeeze()
                window["output"].update(value=definition)
                window["output_reci"].update(value=values["input"])
                window["input"].update(value="")

            else:
                window["output"].update(
                    value="This word does not exist in dictionary,or try lowercase.")
                window["output_reci"].update(value=values["input"])
