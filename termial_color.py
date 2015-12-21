#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
Print colorful words to termial, make prints easy to be distinguished.

See http://stackoverflow.com/questions/287871/print-in-terminal-with-colors-using-python.
In that page, there are a few tools which are more convenient to use.
"""


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    @classmethod
    def color_print(cls, level, msg):
        print level + msg + cls.ENDC


if __name__ == "__main__":
    bcolors.color_print(bcolors.WARNING, "Computer science!")
