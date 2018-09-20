# Shell Lab

This directory contains:
* python code that implements the requiered shell
* The program runs runs a shel that can run simple commands, input/output redirects, "cd", and pipes

The code asks for an input:
1. It either prints whatever is in PS1 but if its empty it prints "$ "
2. If the user types exit the code stops
2. If the input contains a '$' it replaces it and the string tht directly follwos with that strings environmental variable
3. if the input has '>' or '<' it does the corresponding redirect
4. if there is a '=' then it expects an environmental variable to be changed 
5. if user typpes cd it expects a change in directory

This lab contains the following files:
 * shell.py: the shell code

To run:
~~~
$ ./shell.py
~~~

What Worked for me after code was ran:
~~~
$ /bin/uname
Linux
$ uname
Linux
$ ls < ./
shell.py
$ ls > output.txt
$ cat output.txt
output.txt
shell.py
$ cd /
$ pwd
/
~~~

# Known Errors #
Cannot do redirects, change directory, and change environmental variables at the same time
