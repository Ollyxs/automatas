import time
import ej01_constant as cs
from ej04_main import *


def return_menu():
    inp = input(cs.QUESTION_RET)
    if inp.isupper():
        inp = inp.lower()
    if inp == 'y':
        print(cs.JUMP_LINE)
        time.sleep(0.1)
        print(cs.RETURN_MENU)
        time.sleep(0.1)
    elif inp == 'n':
        exit_program()
        exit()
    else:
        error_menu()

def exit_program():
    print(cs.JUMP_LINE)
    time.sleep(0.1)
    print(cs.EXIT)
    time.sleep(0.1)

def error_menu():
    print(cs.JUMP_LINE)
    print(cs.ERR)
    time.sleep(0.1)
    print(cs.JUMP_LINE)
    print(cs.RETURN_MENU)
    time.sleep(0.1)
