-=-=-=-=-= **pyASCII, Electra04's ASCII game emulator** =-=-=-=-=-

-= Built in Python 3 =-
-= You can add your own apps =-
-= Does not require TKinter =-
-= Requires pygame =-

-=-=-=-=-= **How to add your own apps to pyASCII** =-=-=-=-=-

-= Make the .py file for your app and put it in the "apps/" directory.
-= Make a function called (name of your file)_main() with no args. Your app's code will go in 
   here. You also won't need to add a function call for your main function, that will be taken 
   care of by pyASCII's main.py file (But feel free to do so if you want to!)
-= If your app requires more than one file, make a folder with the same name as your app. 
   You can put the other files for your app in there.
-= You (probably) won't need to change anything in the main.py file. It will automatically 
   find your app using the "glob" module.