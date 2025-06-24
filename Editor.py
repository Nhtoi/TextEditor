import msvcrt
import sys
import GapBuffer as gp
import FileOperations as fo

isTyping = True
textfile = fo.Operations()
textfile.path = "newtxt.txt"
textField = gp.GapBuffer()


#b'\x03' ctrl + c
#b'\x1a' ctrl + z
#b'\x13' crtl + s
#b'\x17' ctr + w
# b'\x11' ctrl + q


def quitTyping():
    textfile.text = textField.toSave()
    textfile.save()
    return False

def getInput():
    global isTyping
    pressed = ""
    words = ""
    
    while isTyping:
        pressed = msvcrt.getch()
        if pressed in [b'\x00', b'\xe0']:
            arrow = msvcrt.getch()
            #up
            if arrow == b'H':
                sys.stdout.write(f'\x1b[{1}A')
                sys.stdout.flush()
                get_cursor_position()
                textField._movegap(get_cursor_position())
            #down
            elif arrow == b'P':
                sys.stdout.write(f'\x1b[{1}B')
                sys.stdout.flush()
                get_cursor_position()
                textField._movegap(get_cursor_position())
            #left
            elif arrow == b'K':
                if textField.start > 0:
                    sys.stdout.write(f'\x1b[1D')
                    sys.stdout.flush()
                    textField._movegap(textField.start - 1)
            #right
            elif arrow == b'M':
                if textField.end < textField.size:
                    sys.stdout.write(f'\x1b[1C')
                    sys.stdout.flush()
                    textField._movegap(textField.start + 1)
            continue
        #backspace
        elif pressed == b'\x08':
            textField.backspace(textField.start)
            textField.print()
        #quit typing
        elif pressed == b'\x11':
            return quitTyping()
        #ctrl + a
        elif pressed == b'\x01':
            pass
        #printable chars
        elif pressed.decode(errors="ignore").isprintable():
            ch = pressed.decode(errors="ignore")
            textField.insert(textField.start, ch)
            textField.print()

def get_cursor_position():
    pos = (0,0)
    sys.stdout.write('\x1b[6n')
    sys.stdout.flush()

    response = b''
    while True:
        ch = msvcrt.getch()
        if ch == b'\x11':  # Ignore XON
            continue
        response += ch
        if ch == b'R':
            break

    if response.startswith(b'\x1b[') and response.endswith(b'R'):
        try:
            row, col = map(int, response[2:-1].decode().split(';'))
            pos = (row, col)
            return col - 1  # Convert to 0-based column index
        except:
            return 0
    return 0

def Open():
    text = textfile.open()
    textField.create(text)
    getInput()

Open()
