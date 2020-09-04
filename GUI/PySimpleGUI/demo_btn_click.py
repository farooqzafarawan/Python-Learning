import PySimpleGUI as sg

event, values = sg.Window('Login Window',
                          [[sg.T('Enter your Login ID'), sg.In(key='-ID-')],
                           [sg.B('OK'), sg.B('Cancel')]]).read(close=True)

login_id = values['-ID-']

print(login_id)