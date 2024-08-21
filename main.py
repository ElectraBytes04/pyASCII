import glob
import os
def main():
    apps = glob.glob("apps/*.py")
    apps = [os.path.splitext(app)[0] for app in apps]
    builtins = glob.glob("built-in/*.py")
    builtins = [os.path.splitext(builtin)[0] for builtin in builtins]
    def welcome():
        welcome = f"""
+---------------------------------------------------------------+
| pyASCII - Home x | /////////////////////////////////// _ [] x | 
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
        run = input("""
What app would you like to run?
Make sure the app you want to run is currently loaded or is built in to pyASCII.
        """)
    welcome()
main()