#!/usr/bin/env python3
#A shell's primary job is to ask a user what program to run next, and then to dispatch a new process to run it.

import os, sys, time, re

def parse(input):
    args = input.split()
    if '>' in input:
        os.close(1)
        sys.stdout = open(args[args.index('>')+1],'w')
        fd = sys.stdout.fileno()
        os.set_inheritable(fd,True)
        
        execute                 

    else:
        execute(args)

def execute(args):
    os.execve(args[0],args,os.environ)

def main(input):
    rc = os.fork()

    if rc < 0:
        os.write(2, ("fork failed, returning %d\n" % rc).encode())
        sys.exit(1)

    elif rc == 0:
        parse(input)
        os.write(2, ("Child: Could not exec %s\n" % args[0]).encode())
        sys.exit(1)

    else:                           # parent (forked ok)
        childPidCode = os.wait()

#----------MAIN----------
pid = os.getpid()

input = input("$")
#args = input.split()

main(input)
