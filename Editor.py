import msvcrt
import sys
import GapBuffer as gp
isTyping = True
Pos = (0,0)

#b'\xe0M' Right Arrow
#Backspace b'\x08'
#b'\xe0K' Left Arrow
#b'\xe0H' # Up Arrow
#b'\xe0P # Down Arrow
#Press q to quit
#b'\x03' ctrl + c
#b'\x1a' ctrl + z
#b'\x13' crtl + s
#b'\x17' ctr + w
# b'\x11' ctrl + q
#I feel like this function needs to constantly update the gapbuffer

textField = gp.GapBuffer()
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
                sys.stdout.write(f'\x1b[{1}D')
                sys.stdout.flush()
                get_cursor_position()
                textField._movegap(get_cursor_position())
            #right
            elif arrow == b'M':
                sys.stdout.write(f'\x1b[{1}C')
                sys.stdout.flush()
                get_cursor_position()
                textField._movegap(get_cursor_position())
            continue
        #backspace
        elif pressed == b'\x08':
            textField.backspace(get_cursor_position())
        #quit typing
        elif pressed == b'\x11':
            isTyping = False
            break
        #ctrl + a
        elif pressed == b'\x01':
            pass
        #type actual "printable" characters
        #0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
        elif pressed.decode(errors="ignore").isprintable():
            ch = pressed.decode(errors="ignore")
            pos = get_cursor_position()
            textField.insert(pos, ch)
            sys.stdout.flush()

#should pass this to the gapbuffer so get the exact position of the edit/insertion/delete
def get_cursor_position():
    global Pos
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
            Pos = (row, col)
            return col - 1  # Convert to 0-based column index
        except:
            return 0
    return 0

getInput()
get_cursor_position()