import sys

if sys.platform == "win32":
    import msvcrt
    getch = msvcrt.getch
else:
    import tty, termios
    def getch():
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            return sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)

print("Start typing (press Enter to finish):")

def input_loop(gameinput_func):
    while True:
        char = getch()
        # if char == 'my super secret escape code':
        #   do_some_launcher_magic(char)
        # else:
        gameinput_func(char)
        print(f"{char}")
