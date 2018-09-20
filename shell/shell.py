#!/usr/bin/env python3
#A shell's primary job is to ask a user what program to run next, and then to dispatch a new process to run it.

import os, sys, time, re

def parse(uinput):
    args = uinput.split()
    
    #Checks for environmental variables $
    for arg in args:
        if '$' in arg:
            arg = arg.replace("$","")
            try:
                uinput = uinput.replace('$' + arg,os.environ[arg])
            except KeyError:
                return
                #os.write(2, ("Key Error: %s" % arg).encode())
    args = uinput.split()

    if 'exit' in uinput:
        return
    #Handles output redirect
    elif '>' in uinput:
        os.close(1)
        sys.stdout = open(args[args.index('>')+1],'w')
        fd = sys.stdout.fileno()
        os.set_inheritable(fd,True)      
        execute(args[:args.index('>')])

    #Handles input redirect
    elif '<' in uinput:
        uinput = uinput.replace('<','')
        args = uinput.split()
        execute(args)
    #Handle pipes
    elif '|' in uinput:
        pass
    #Default
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
        os.write(2, ("Child: Could not exec %s\n" % uinput.split()[0]).encode())
        sys.exit(1)

#----------MAIN----------
    
user_input = ""

while 'exit' not in user_input:
    try:
        user_input = input(os.environ['PS1'])
    except KeyError:
        user_input = input('$ ')
    
    #Handles directory change
    if 'cd' in user_input:
        args = user_input.split()
        os.chdir(args[1])
    #Handles changing environmental variables
    elif '=' in user_input:
        uinput = user_input.replace(" ","")
        args = user_input.split("=")
        os.environ[args[0]] = args[1].replace("\"","")
        #print(os.environ[arg[0]])
    else:
        rc = os.fork()

        if rc < 0:
            os.write(2, ("fork failed, returning %d\n" % rc).encode())
            sys.exit(1)
        elif rc == 0:
            parse(user_input)
            sys.exit(1)
        else:
            childPidCode = os.wait()
