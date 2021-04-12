def infiniteloop():

    import PySimpleGUI as sg
    from pythonping import ping
    import sys

#Layout van de GUI bepalen
    layout = [  [sg.Text("ICMP Availibility Checker")], 
                [sg.Listbox(values=('8.8.8.8 (Remote host)', '127.0.0.1 (localhost)', 'google.nl (Remote host with DNS)'), size=(30, 6), key='_LISTBOX_')],  
                [sg.Button("OK")]
            ]

    # venster creeren
    window = sg.Window("Availibility Checker", layout).Finalize()

    # een loop voor de "OK", of de "X" (sluiten)
    while True:
        event, values = window.read()

        # verder gaan met programma als er op "OK" word gedrukt
        if event == "OK":
            break
        # programma beeindigen als venster word gesloten
        elif event == WIN_CLOSED:
            sys.exit()

# values variable omzetten naar een string (ik weet niet hoe je anders deze variable kan verwerken)
    values = str(values)

# het gekozen item aan de varible 'pingert' toewijzen, bij geen selectie begint de code opnieuw
    if   'google.nl' in values:
        pingert = 'google.nl'

    elif   '127.0.0.1' in values:
        pingert = '127.0.0.1'

    elif   '8.8.8.8' in values:
        pingert = '8.8.8.8'

    else:
        return
            
# ping the host, and show popup with result            
    pingresult = str(ping(pingert, verbose=True))
    sg.popup(pingresult)    

# infinite loop, zodat het programma niet na 1x afsluit
while True:
    infiniteloop()