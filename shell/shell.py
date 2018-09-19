#!/usr/bin/env python3
#A shell's primary job is to ask a user what program to run next, and then to dispatch a new process to run it.

import os, sys, time, re

def parse(uinput):
    args = uinput.split()
    if '>' in uinput:
        os.close(1)
        sys.stdout = open(args[args.index('>')+1],'w')
        fd = sys.stdout.fileno()
        os.set_inheritable(fd,True)
        
        execute                 

    else:
        execute(args)

def execute(args):
    #try to execute with given directory
    try:
        os.execve(args[0],args,os.environ)
    except FileNotFoundError:
        pass
    #try to execute with directories in PATH
    for dir in re.split(":", os.environ['PATH']):
        program = "%s/%s" % (dir, args[0])
        try:
            os.execve(program, args, os.environ)
        except FileNotFoundError:  
            pass 
        
def main(uinput):
    rc = os.fork()

    if rc < 0:
        os.write(2, ("fork failed, returning %d\n" % rc).encode())
        sys.exit(1)

    elif rc == 0:
        parse(uinput)
        os.write(2, ("Child: Could not exec %s\n" % args[0]).encode())
        sys.exit(1)

    else:                           # parent (forked ok)
        childPidCode = os.wait()

#----------MAIN----------
pid = os.getpid()

user_input = input("$")

while 'exit' not in user_input:
    main(user_input)

    user_input = input("$")
