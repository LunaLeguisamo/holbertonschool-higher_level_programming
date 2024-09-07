#!/usr/bin/python3

import sys

if __name__ == "__main__":
    add = 0
    len = len(sys.argv)
    for arguments in sys.argv[1:]:
        add += int(arguments)
    print("{}" .format(add))