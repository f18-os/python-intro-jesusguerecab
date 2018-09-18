#! /usr/bin/env python3
#A shell's primary job is to ask a user what program to run next, and then to dispatch a new process to run it.

import os, sys, time, re

def execute(argv):
    rc = os.fork()

    if rc < 0:
        os.write(2, ("fork failed, returning %d\n" % rc).encode())
        sys.exit(1)

    elif rc == 0:
        os.write(1, ("Child: My pid==%d.  Parent's pid=%d\n" %
                     (os.getpid(), pid)).encode())
        #program = "%s%s" % (dir, args[0])
        os.write(1, ("Child:  ...trying to exec %s\n" % program).encode())
        os.execve(program, args, os.environ)
        os.write(2, ("Child: Could not exec %s\n" % args[0]).encode())
        sys.exit(1)

    else:                           # parent (forked ok)
        childPidCode = os.wait()

#----------MAIN----------
pid = os.getpid()

input = input("$")
args = input.split()

execute(args)
