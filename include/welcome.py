import shutil

def get_termsize():
     size = shutil.get_terminal_size((80, 20))
     return size.columns

columns = get_termsize()

def main(usermade, builtin):
    get_termsize()
    if (columns <= 80):
        welcome_80h = f"""
+---------------------------------------------------------------+
| pyASCII - Home x | 04/04/04/04/04/04/04/04/04/04/04/04 _ [] x |
|===============================================================|
|                                                               |
| -=-=-= pyASCII - ver 0.0.0 - created by ElectraBytes04 =-=-=- |
|           Hello! Thank you for using pyASCII.                 |
|                                                               |
|-=> Currently loaded user-made apps:                           |
| {usermade}
|                                                               |
|===============================================================|
|                                                               |
|-=> And the built-in apps:                                     |
| {builtin}
|                                                               |
+---------------------------------------------------------------+
"""
        print(welcome_80h)
