#!/usr/bin/env python3

import operator
import readline
import logging
import colorama
from colorama import Fore, Style
from termcolor import colored

colorama.init()
logging.basicConfig(filename="rpn.log",
        format='%(asctime)s|%(message)s',
        filemode='w')
logger=logging.getLogger()
logger.setLevel(logging.DEBUG)

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow,
    '%': operator.mod,
}

def calculate(myarg):
    stack = list()
    for token in myarg.split():
        try:
            token = int(token)
            stack.append(token)
        except ValueError:
            function = operators[token]
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = function(arg1, arg2)
            stack.append(result)
        logging.debug(stack)
    if len(stack) != 1:
        raise TypeError("Too many parameters")
    return stack.pop()

def main():
    print(Style.BRIGHT + "RPN Calculator" + Style.RESET_ALL)
    while True:
        result = calculate(input(colored("rpn calc> ", 'cyan')))
        
        if result < 0:
            print("Result:", colored(result, 'red'))
        elif result == 0:
            print("Result: ", colored(result, 'blue'))
        else:
            print("Result: ", colored(result, 'green'))

if __name__ == '__main__':
    main()
