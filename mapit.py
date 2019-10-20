#! python3
import webbrowser, sys, pyperclip


def navigate():
    sys.argv

    #check if command line arguments were passed
    if len(sys.argv) > 1:
        # ['mapit.py', '90', 'Dulan', 'st.'] -> '90 Dulan St.'
        address = ' '.join(sys.argv[1:])
    else:
        address = pyperclip.paste()

    #https://www.google.com/maps/place/<ADDRESS>
    webbrowser.open('https://www.google.com/maps/place/' + address)

navigate()
