import PySimpleGUI as sg
import YouTube_Download_Functions as yt_fun

# Popups and guessing are suppressed, just getting an exception by key error
sg.set_options(suppress_raise_key_errors=False, suppress_error_popups=True, suppress_key_guessing=True)

sg.theme("Dark")

layout = [[sg.Text("Enter your YT link here:")],
          [sg.Input(size=(30, 1), key='-URL-')],
          [sg.Button('Download'), sg.Exit('Exit')]]


window = sg.Window("YouTube Downloader", layout)

while True:
    event, values = window.read()

    if event in (sg.WIN_CLOSED, 'Exit'):
        break

    if event == 'Download':
        url = values['-URL-']
        yt_fun.run_engine(url)
