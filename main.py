import time
import os
import importlib.util

def main():
    apps = os.listdir('apps')
    builtins = os.listdir('built-in')

    def welcome():
        welcome = f"""
+---------------------------------------------------------------+
| pyASCII - Home x | 04/04/04/04/04/04/04/04/04/04/04/04 _ [] x |
|===============================================================|
|                                                               |
| -=-=-= pyASCII - ver 0.0.0 - created by ElectraBytes04 =-=-=- |
|           Hello! Thank you for using pyASCII.                 |
|                                                               |
|-=> Currently loaded user-made apps:                           |
| {apps}
|                                                               |
|===============================================================|
|                                                               |
|-=> And the built-in apps:                                     |
| {builtins}
|                                                               |
+---------------------------------------------------------------+
"""
        print(welcome)
    welcome()

    def appload():
        try:
            try:
                print("Looking in apps/user-made/")
                time.sleep(1)
                spec = importlib.util.spec_from_file_location(f"{run}", f"apps/user-made/{run}/{run}.py")
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                return module
            except:
                print("Looking in apps/built-in/")
                time.sleep(1)
                spec = importlib.util.spec_from_file_location(f"{run}", f"apps/built-in/{run}/{run}.py")
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                return module
        except:
            print("Could not find the app you tried to load\nDid you spell the name of the app correctly?")

    run = input("""
Please enter the command you would like to run.
For command help, go to the 'command-help' file in /data/.
""")
    appload()
main()
