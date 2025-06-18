import msvcrt
import sys
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
            #down
            elif arrow == b'P':
                sys.stdout.write(f'\x1b[{1}B')
                sys.stdout.flush()
                get_cursor_position()
            #left
            elif arrow == b'K':
                sys.stdout.write(f'\x1b[{1}D')
                sys.stdout.flush()
                get_cursor_position()
            #right
            elif arrow == b'M':
                sys.stdout.write(f'\x1b[{1}C')
                sys.stdout.flush()
                get_cursor_position()
            continue
        #backspace
        elif pressed == b'\x08':
            words = words[:-1]
        #quit typing
        elif pressed == b'\x11':
            isTyping = False
            break
        #type actual "printable" characters
        #0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
        elif pressed.decode(errors="ignore").isprintable():
            words += pressed.decode(errors="ignore")
                
        sys.stdout.write(f'\r' + words + ' ')
        sys.stdout.flush()

def get_cursor_position():
    global Pos
    sys.stdout.write('\x1b[6n')
    sys.stdout.flush()

    response = b''
    while True:
        ch = msvcrt.getch()
        if ch == b'\x11':
            continue
        response += ch
        if ch == b'R':
            break
    if response.startswith(b'\x1b[') and response.endswith(b'R'):
        try:
            row, col = map(int, response[2:-1].decode().split(';'))
            currPos = (row, col)
            old_row, old_col = Pos
            new_row, new_col = currPos
            row_diff = new_row - old_row
            col_diff = new_col - old_col
            #get updated cursor position
            return (row_diff, col_diff)
        except:
            return None, None
    return None, None


print()
getInput()
#can be called to get cursor position for gap buffer
#row_diff = row
#col_diff = column
get_cursor_position()

