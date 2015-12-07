# python-terminal-sublime

This is an installation script which adds two build systems to let you run python 2 and python 3 code in a native system terminal instead of within a REPL. Normally a REPL is fine, but under certain circumstances with IO there can be exceptions. There are advantages and disadvantages to doing it this way, but I find that the advantages outweight the disadvantages.

## Prereqs
1. Install Sublime Text 3 and *open it* at least once.
2. Install Python 3, and configure your path to be able to run python 3 from a terminal. Ensure that the py launcher is configured properly, such that running `py -2` spawns a python2 shell, and `py -3` spawns a python3 shell.

##Installation
From a terminal, run the following (after navigating to the proper directory):

```bash
python3 python_terminal_installer.py
```

_Note, the current version of the script also seems to run with python2, but compatability isn't guaranteed for future versions_

Expected execution time for the installer is 2-3 minutes; the vast majority of this is a search for your Sublime install directory. Upon successful completion of the installation, you'll see a message in your terminal with the postreqs, duplicated below.

##Postreqs

Go to `Sublime->Tools->Build System` and select `python_terminal` for Python3, and `python_terminal_2` for Python2

That's it! You'll now be able to use `CTRL + B` [`CMD + B` on Mac OS X] to execute your python files from within sublime. Give it a shit!

Windows: Use `CTRL + C` to exit the interpreter (>>> prompt) and close the terminal
OS X: Use `CTRL + D` to exit the interpreter (>>> prompt), and `CMD + Q` to exit the window
Linux: Use `CTRL + D` to exit the interpreter (>>> prompt) and close the terminal

Please direct any bugs, suggestions, or feedback to the issue tracker on the GitHub page:
http://github.com/VasuAgrawal/python-terminal-sublime
