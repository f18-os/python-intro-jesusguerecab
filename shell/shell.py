#!/usr/bin/env python3
#A shell's primary job is to ask a user what program to run next, and then to dispatch a new process to run it.

import os, sys, time, re

def parse(uinput):
    args = uinput.split()
    for arg in args:
        if '$' in arg:
            arg = arg.replace("$","")
            try:
                uinput = uinput.replace(arg,os.environ[arg])
            except KeyError:
                os.write(2, ("Key Error: %s" % arg).encode())
    args = uinput.split()
    if '>' in uinput:
        os.close(1)
        sys.stdout = open(args[args.index('>')+1],'w')
        fd = sys.stdout.fileno()
        os.set_inheritable(fd,True)
              
        execute(args[:args.index('>')])
    elif '=' in uinput:
        uinput = uinput.replace(" ","")
        args = uinput.split("=")
        os.environ[args[0]] = args[1]
        #print(os.environ['a'])
        sys.exit(1)
    elif 'cd' in uinput:
        os.chdir(args[1])
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
        
def fork(uinput):
    rc = os.fork()

    if rc < 0:
        os.write(2, ("fork failed, returning %d\n" % rc).encode())
        sys.exit(1)

    elif rc == 0:
        parse(uinput)
        os.write(2, ("Child: Could not exec %s\n" % uinput.split()[0]).encode())
        sys.exit(1)

    else:                           # parent (forked ok)
        childPidCode = os.wait()

#----------MAIN----------
pid = os.getpid()

user_input = input("$")

os.environ['a'] = "2"

while 'exit' not in user_input:
    fork(user_input)

    user_input = input("$")
