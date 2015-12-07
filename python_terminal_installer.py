#!/usr/bin/env python3

###############################################################################
# 									README:
#
# Prereqs:
# 	1) Install Sublime Text 3 and open it
# 	2) Install Python 3, and configure your path to be able to run python3
# 	   from a terminal and get an interactive shell
#
# To install with this script, simply open a shell and type in
# 		python3 python_terminal_installer.py
#
# Expected execution time for this file is approximately 2-3 minutes.
# Upon successful completion of the installation, you'll receive a message
# with the postreqs. They are duplicated below.
#
# Postreqs:
# 	Go to Sublime->Tools->Build System and select python_terminal
#
# That's it! You'll now be able to use CTRL + B [CMD + B on Mac OS X]
# to execute your python files. Give it a shot!
#
# Windows: Use CTRL + C to exit the >>> prompt, and Alt + Space, c to close
# OS X: Use CTRL + D to exit >>> the prompt, and CMD + Q to exit the window
# Linux: Use CTRL + D to exit the prompt
#
# Please direct any bugs, suggestions, or feedback at the issue tracker
# in github: http://github.com/VasuAgrawal/python-terminal-sublime
#
###############################################################################

import os
import sys
from sys import platform as _platform

# Used on all 3 operating systems
build_name = "python_terminal.sublime-build"
build_name_2 = "python_terminal_2.sublime-build"
python_terminal__sublime_build = """\
{
    "selector": "source.python",

    "linux": {
        "cmd": ["%s", "$file"]
    },
    "osx": {
        "cmd": ["%s", "$file"]
    },
    "windows": {
        "cmd": ["%s", "$file"]
    }
}"""

# Used on windows
bat_name = "python_terminal.bat"
python_terminal__bat = """\
@echo off
start py.exe -3 -i %1
exit
"""
bat_name_2 = "python_terminal_2.bat"
python_terminal_2__bat = """\
@echo off
start py.exe -2 -i %1
exit
"""
# Used on linux
shell_name = "python_terminal.sh"
python_terminal__sh = """\
#!/usr/bin/env bash
echo Attempting to build / execute file ...

name=$(printf %q "$1")
to_exec="python3 -i $name"

if gnome-terminal -e "$to_exec" 2> /dev/null
then
    echo "Executing in gnome-terminal"
elif konsole -e "$to_exec" 2> /dev/null
then
    echo "Executing in konsole"
elif xterm -e "$to_exec" 2> /dev/null
then
    echo "Executing in xterm"
elif x-terminal-emulator -e "$to_exec" 2> /dev/null
then
    echo "Executing in default terminal"
else
    echo "Unable to find a terminal to execute in!
    exit 42

echo Executed file!
"""

# Credit for the following bash script to:
#http://stackoverflow.com/questions/4404242/programmatically-launch-terminal-app-with-a-specified-command-and-custom-colors
osx_terminal_name = "term.sh"
osx_terminal_text = """\
#!/bin/sh

echo '
on run argv
  if length of argv is equal to 0
    set command to ""
  else
    set command to item 1 of argv
  end if

  if length of argv is greater than 1
    set profile to item 2 of argv
    runWithProfile(command, profile)
  else
    runSimple(command)
  end if
end run

on runSimple(command)
  tell application "Terminal"
    activate
    set newTab to do script(command)
  end tell
  return newTab
end runSimple

on runWithProfile(command, profile)
  set newTab to runSimple(command)
  tell application "Terminal" to set current settings of newTab to (first settings set whose name is profile)
end runWithProfile
' | osascript - "$@" > /dev/null
"""

osx_python_terminal__sh_name = "osx_python_terminal.sh"
osx_python_terminal__sh = """\
#!/usr/bin/env bash
echo Attempting to build / execute file ...

name=$(printf %%q "$1")
%s "python3 -i $name"

echo Executed file!
"""

###############################################################################

def find_sublime(path):
    home = os.path.expanduser("~")
    print("Found sublime directory at", home)
    for root, dirnames, filenames in os.walk(path):
        if ("Sublime Text 3" in root or
            "sublime-text-3" in root):
            if ("Packages" in root and "User" in dirnames):
                return os.path.join(root, "User")
    print("""\


Unable to find Sublime installation directory.
Please ensure you have Sublime Text 3 installed,
and that you have opened it at least once:

    http://www.sublimetext.com/3

""")
    return None


def install():
    print("Beginning install ...")
    sublime_home = find_sublime(os.path.expanduser("~"))
    if sublime_home is None:
        return

    if _platform == "linux" or _platform == "linux2":
        print("Installing for linux ...")
        sh_path = os.path.join(sublime_home, shell_name)
        sh_path_escaped = sh_path.replace(os.sep, os.sep + os.sep)
        sh_text = python_terminal__sh

        with open(sh_path, "w") as out:
            out.write(sh_text)
            out.close()

        # Need to make it executable
        os.chmod(sh_path, 0o777)

        build_path = os.path.join(sublime_home, build_name)
        build_text = python_terminal__sublime_build % (sh_path, "", "")

        with open(build_path, "w") as out:
            out.write(build_text)
            out.close()

    elif _platform == "darwin":
        print("Installing for OS X ...")
        term_path = os.path.join(sublime_home, osx_terminal_name)
        term_path_escaped = term_path.replace(os.sep, os.sep + os.sep)
        term_path_space_escaped = term_path.replace(" ", "\ ")
        term_text = osx_terminal_text

        with open(term_path, "w") as out:
            out.write(term_text)
            out.close()

        os.chmod(term_path, 0o777)

        sh_path = os.path.join(sublime_home, osx_python_terminal__sh_name)
        sh_path_escaped = sh_path.replace(os.sep, os.sep + os.sep)
        sh_text = osx_python_terminal__sh % term_path_space_escaped

        with open(sh_path, "w") as out:
            out.write(sh_text)
            out.close()

        os.chmod(sh_path, 0o777)

        build_path = os.path.join(sublime_home, build_name)
        build_text = python_terminal__sublime_build % ("", sh_path, "")

        with open(build_path, "w") as out:
            out.write(build_text)
            out.close()

    elif _platform == "win32":
        print("Installing for Windows ...")
        # Python 3 installer
        bat_path = os.path.join(sublime_home, bat_name)
        bat_path_escaped = bat_path.replace(os.sep, os.sep + os.sep)
        bat_text = python_terminal__bat

        with open(bat_path_escaped, "w") as out:
            out.write(bat_text)
            out.close()

        build_path = os.path.join(sublime_home, build_name)
        build_path_escaped = build_path.replace(os.sep, os.sep + os.sep)
        build_text = python_terminal__sublime_build % ("", "", bat_path_escaped)

        with open(build_path_escaped, "w") as out:
            out.write(build_text)
            out.close()

        # Python 2 installer
        bat_path = os.path.join(sublime_home, bat_name_2)
        bat_path_escaped = bat_path.replace(os.sep, os.sep + os.sep)
        bat_text = python_terminal_2__bat

        with open(bat_path_escaped, "w") as out:
            out.write(bat_text)
            out.close()

        build_path = os.path.join(sublime_home, build_name_2)
        build_path_escaped = build_path.replace(os.sep, os.sep + os.sep)
        build_text = python_terminal__sublime_build % ("", "", bat_path_escaped)

        with open(build_path_escaped, "w") as out:
            out.write(build_text)
            out.close()

    print("Installed successfully!")
    print("""\

Final step:
    Go to Sublime->Tools->Build System and select python_terminal

That's it! You'll now be able to use CTRL + B [CMD + B on Mac OS X]
to execute your python files. Give it a shot!

Windows: Use CTRL + C to exit the >>> prompt, and Alt + Space, c to close
OS X: Use CTRL + D to exit >>> the prompt, and CMD + Q to exit the window
Linux: Use CTRL + D to exit the prompt

Please direct any bugs, suggestions, or feedback at github issue tracker:
http://github.com/VasuAgrawal/python-terminal-sublime
""")

install()
