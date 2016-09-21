'''
TinyDOS
Author: Kelvin Chris Lau, 9682466, klau158
'''

import sys

print("-----------------------------------")
print("        Welcome To TinyDOS")
print("")
print("      by Kelvin Lau, 9682466")
print("-----------------------------------")

while True:
    print("> ", end="")
    
    # read user input and remove leading/trailing white space
    
    command = input().strip()
    
    if command == "quit":
        sys.exit()
    else:
        print("Unknown command")