import include.welcome
import include.info

import json

import time
import os
import importlib.util

def appload(app):
        try:
            try:
                print("Looking in apps/user-made/")
                time.sleep(1)
                spec = importlib.util.spec_from_file_location(
                    f"{app}", f"apps/user-made/{app}/{app}.py"
                )
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                return module
            except:
                print("Looking in apps/built-in/")
                time.sleep(1)
                spec = importlib.util.spec_from_file_location(
                    f"{app}", f"apps/built-in/{app}/{app}.py"
                )
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                return module
        except:
            print(include.info.appload_error)

def main():
    usermade = os.listdir('apps/user-made')
    builtin = os.listdir('apps/built-in')

    include.welcome.main(f"{usermade}", f"{builtin}")

    run = input(include.info.command_help)
    appload(f"{run}")    

main()
