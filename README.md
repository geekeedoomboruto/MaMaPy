# MaMaPy
Just a Python in french and more easier, i made it to help my mom understand programming, it's a very basic language, more like a plugin for Python
# Version
- MaMaPy 0.0.1 (with MaMaShell.py)
- MaMaPy 0.0.2 (with shell.py)
- MaMaPy 0.0.3 (with shell.py)
- MaMaPy 0.0.4 (with shell_v2.py)
- MaMaPy FOSV (current version with shell_v2)
# How to execute a MaMaPy code ?
First thing to know is that the extension for a MaMaPy file is .mmp but that you are not obligated to use this file extension.
The command to use when executing a program is: <code>python exec.py execute 'somefile.mmp'</code>.
Suppose that you have a file called looping.mmp, to execute it you write <code>python exec.py execute 'looping.mmp'</code>
# How it works ? 
There is two steps for the execution of the program.
- Translation
- Interpretation
# More precisely
The Translation works with a file named COMP.py, it takes the code, translate the code in python line by line, and then reassemble them.
Then Python interprets in with the exec() function.
Be sure to have a sanitised environnment because my code uses exec() and eval() <code>exec.py</code> knows how to execute python code (in MaMaPy you are not obligated to write MaMaPy code).
