import msvcrt
import sys
isTyping = True
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
        letters = pressed.decode('utf-8')
        if letters.isprintable():
            words += letters
        sys.stdout.write(f'\r' + words + ' ')
        sys.stdout.flush()
        if pressed == b'\xe0':
            arrow = msvcrt.getch()
            if arrow == b'H':
                print("Up Arrow")
            if arrow == b'P':
                print("Down Arrow")
            if arrow == b'K':
                print("Left Arrow")
            if arrow == b'M':
                print("Right Arrow")
        if pressed == b'\x08':
            words = words[:-1]
        if pressed == b'\x11':
            print("Quit")
            isTyping = False
            break
print()
getInput()
