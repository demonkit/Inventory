#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
Print colorful words to termial, make prints easy to be distinguished.
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
