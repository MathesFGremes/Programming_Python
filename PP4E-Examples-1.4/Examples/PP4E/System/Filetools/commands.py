#!/usr/local/bin/python
from sys import argv
from scanfile import scanner
class UnknownCommand(Exception): pass
commands = {'*': 'Ms.', '+': 'Mr.'}

def processLine(line):                      # define a function
    #if line[0] == '*':                      # applied to each line
    #    print("Ms.", line[1:-1])
    #elif line[0] == '+':
    #    print("Mr.", line[1:-1])            # strip first and last char: \n
    #else:
    #    raise UnknownCommand(line)          # raise an exception
    try:
        print(commands[line[0]], line[1:-1]) 
    except KeyError:
        raise UnknownCommand(line)


filename = 'data.txt'
#print('argv[0]: ', argv[0])
#print('argv[1]: ', argv[1])
#print('argv[2]: ', argv[2])
print("len(argv): ", len(argv))
if len(argv) == 2: filename = argv[1]       # allow filename cmd arg
scanner(filename, processLine)              # start the scanner


"""
commands = {'*': 'Ms.', '+': 'Mr.'}     # data is easier to expand than code?

def processLine(line):
    try:
        print(commands[line[0]], line[1:-1])
    except KeyError:
        raise UnknownCommand(line)

scanner(argv[1], processLine)
"""