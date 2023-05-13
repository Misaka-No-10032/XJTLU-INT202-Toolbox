import os
import sys


def clean():
    if sys.platform.startswith('darwin') or sys.platform.startswith('linux'):
        os.system("clear")
    else:
        os.system("cls")
