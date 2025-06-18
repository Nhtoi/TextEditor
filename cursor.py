import msvcrt
import sys
#test file to see how the cursor could work


def move_cursor_up(n):
    sys.stdout.write(f'\x1b[{n}A')

def move_cursor_down(n):
    sys.stdout.write(f'\x1b[{n}B')

def move_cursor_right(n):
    sys.stdout.write(f'\x1b[{n}C')

def move_cursor_left(n):
    sys.stdout.write(f'\x1b[{n}D')

def move_cursor_to_position(row, col):
    sys.stdout.write(f'\x1b[{row};{col}H')

def clear_screen():
    sys.stdout.write('\x1b[6n')
    sys.stdout.flush()
    


