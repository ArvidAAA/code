import PySimpleGUI as sg
sg.theme('Topanga')      # Add some color to the window

# Very basic window.  Return values using auto numbered keys

hej = input("Y/N: ")

if hej == "Y":
    layout1 = [
    [sg.Text('Please enter your Name, Address, Phone')],
    [sg.Text('Name 1', size=(15, 1)), sg.InputText()],
    [sg.Text('Address 1', size=(15, 1)), sg.InputText()],
    [sg.Text('Phone 1', size=(15, 1)), sg.InputText()],
    [sg.Submit(), sg.Cancel()]
]

    window = sg.Window('Simple data entry window', layout1)
    event, values = window.read()
    window.close()
    print(event, values[0], values[1], values[2])    # the input data looks like a simple list when auto numbered
    layout2 = [
    [sg.Text('Please enter your Name, Address, Phone')],
    [sg.Text('Name 2', size=(15, 1)), sg.InputText()],
    [sg.Text('Address 2', size=(15, 1)), sg.InputText()],
    [sg.Text('Phone 2', size=(15, 1)), sg.InputText()],
    [sg.Submit(), sg.Cancel()]
]

    window = sg.Window('Simple data entry window', layout2)
    event, values = window.read()
    window.close()
    print(event, values[0], values[1], values[2])    # the input data looks like a simple list when auto numbered

else:
    print("Exit")

