'''
TinyDOS
Author: Kelvin Chris Lau, 9682466, klau158
'''

import sys

QUIT = "quit"
FORMAT = "format"
RECONNECT = "reconnect"
LS = "ls"
MKFILE = "mkfile"
MKDIR = "mkdir"
APPEND = "append"
PRINT = "print"
DELFILE = "delfile"
DELDIR = "deldir"

ARG_CMD_LIST = [FORMAT, RECONNECT, LS, MKFILE, MKDIR, APPEND, PRINT, DELFILE, DELDIR]

print("-----------------------------------")
print("        Welcome To TinyDOS")
print("")
print("      by Kelvin Lau, 9682466")
print("-----------------------------------")

while True:
    print("> ", end="")
    
    # read user input and remove leading/trailing white space and split it
    userInput = input().strip().split(' ')
    command = userInput[0].lower()
        
    if command == QUIT:
        sys.exit()
        
    else:
        
        for cmd in ARG_CMD_LIST:
            match = cmd == command
            if match:
                break
            
        if not match:
            print("Unknown command: " + command)
            
        else:
            
            if len(userInput) < 2:
                print("ERROR: " + command + " takes a single argument")
                continue
            
            if len(userInput) > 2:
                print("WARNING: " + command + " takes a single argument... using first argument")
        
            if command == FORMAT:
                print("formatting")
                
            elif command == RECONNECT:
                print("reconnecting")
                
            elif command == LS:
                print("ls ing")
                
            elif command == MKFILE:
                print("mkingfile")
            
            elif command == MKDIR:
                print("mkingdir")
                
            elif command == APPEND:
                print("appending")
                
            elif command == PRINT:
                print("printing print")
                
            elif command == DELFILE:
                print("dellingfile")
                
            elif command == DELDIR:
                print("dellingdir")